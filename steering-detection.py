import jetson.inference
import jetson.utils
from adafruit_servokit import ServoKit

object_detection = jetson.inference.detectNet("coco-bottle", threshold=0.75)
camera = jetson.utils.videoSource("csi://0")      # '/dev/video0' for V4L2
camera.Close()
display = jetson.utils.videoOutput("display://0")

#kit = ServoKit(channels=8)

camera.Open()

speed, old_speed = 0.12, 0.12
angle, old_angle = 90, 90
#kit.servo[0].angle = angle
while display.IsStreaming():
	img = camera.Capture()

	detections = object_detection.Detect(img)

	for detection in detections:
		speed = 0
		if detection.ClassID == 1:
			angle = (int(((detection.Center[0] / camera.GetWidth())*180)/10))*10
			speed = 0.12
			print(1)
	if speed != old_speed:
		#kit.continuous_servo[1].throttle = speed
		old_speed = speed
	if angle != old_angle:
		#kit.servo[0].angle = angle
		old_speed = angle
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(object_detection.GetNetworkFPS()))
	display.Render(img)
camera.Close()
