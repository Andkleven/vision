import jetson.inference
import jetson.utils
import numpy as np


class segmentationBuffers:
    def __init__(self, net):
        self.net = net
        self.mask = None
        self.overlay = None
        self.composite = None
        self.class_mask = None
        
        self.use_stats = "store_true"
        self.use_mask = "mask" in "overlay,mask"
        self.use_overlay = "overlay" in "overlay,mask"
        self.use_composite = self.use_mask and self.use_overlay
        
        if not self.use_overlay and not self.use_mask:
            raise Exception("invalid visualize flags - valid values are 'overlay' 'mask' 'overlay,mask'")
             
        self.grid_width, self.grid_height = net.GetGridSize()	
        self.num_classes = net.GetNumClasses()

    @property
    def output(self):
        if self.use_overlay and self.use_mask:
            return self.composite
        elif self.use_overlay:
            return self.overlay
        elif self.use_mask:
            return self.mask
            
    def Alloc(self, shape, format):
        if self.overlay is not None and self.overlay.height == shape[0] and self.overlay.width == shape[1]:
            return

        if self.use_overlay:
            self.overlay = jetson.utils.cudaAllocMapped(width=shape[1], height=shape[0], format=format)

        if self.use_mask:
            mask_downsample = 2 if self.use_overlay else 1
            self.mask = jetson.utils.cudaAllocMapped(width=shape[1]/mask_downsample, height=shape[0]/mask_downsample, format=format) 

        if self.use_composite:
            self.composite = jetson.utils.cudaAllocMapped(width=self.overlay.width+self.mask.width, height=self.overlay.height, format=format) 

        if self.use_stats:
            self.class_mask = jetson.utils.cudaAllocMapped(width=self.grid_width, height=self.grid_height, format="gray8")
            self.class_mask_np = jetson.utils.cudaToNumpy(self.class_mask)
            
    def ComputeStats(self):
        if not self.use_stats:
            return
            
        # get the class mask (each pixel contains the classID for that grid cell)
        self.net.Mask(self.class_mask, self.grid_width, self.grid_height)

        # compute the number of times each class occurs in the mask
        class_histogram, _ = np.histogram(self.class_mask_np, self.num_classes)

        for n in range(self.num_classes):
            percentage = float(class_histogram[n]) / float(self.grid_width * self.grid_height)

seg = jetson.inference.segNet("fcn-resnet18-deepscene-576x320")


# create buffer manager
buffers = segmentationBuffers(seg)

# create video sources & outputs
input = jetson.utils.videoSource("csi://0")
input.Close()
output = jetson.utils.videoOutput("display://0")

input.Open()
# process frames until user exits
while True:
	# capture the next image
	img_input = input.Capture()

	# allocate buffers for this size image
	buffers.Alloc(img_input.shape, img_input.format)

	# process the segmentation network
	seg.Process(img_input)

	# generate the overlay
	if buffers.overlay:
		seg.Overlay(buffers.overlay)

	# generate the mask
	if buffers.mask:
		seg.Mask(buffers.mask)

	# composite the images
	if buffers.composite:
		jetson.utils.cudaOverlay(buffers.overlay, buffers.composite, 0, 0)
		jetson.utils.cudaOverlay(buffers.mask, buffers.composite, buffers.overlay.width, 0)

	# render the output image
	output.Render(buffers.output)

	# update the title bar
	output.SetStatus("Network {:.0f} FPS".format(seg.GetNetworkFPS()))

	# print out performance info
	jetson.utils.cudaDeviceSynchronize()
	seg.PrintProfilerTimes()

	buffers.ComputeStats()
    
	# exit on input/output EOS
	if not input.IsStreaming() or not output.IsStreaming():
		break