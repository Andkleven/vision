### Jetson Nano
1. https://developer.nvidia.com/blog/realtime-object-detection-in-10-lines-of-python-on-jetson-nano/
2. https://www.jetsonhacks.com/2019/10/23/install-ros-on-jetson-nano/
3. https://github.com/dusty-nv/ros_deep_learning


### Onnx
1. Downlaod https://github.com/lutzroeder/netron
2. Se run_onnx_model.py

### Install Jetson Inference
1. https://github.com/dusty-nv/jetson-inference

### Setup Project

1.  ```console
    git clone https://github.com/Andkleven/vision.git
    ```
1.  ```console
    cd vision
    ```
1.  Download pretrained model [her](https://drive.google.com/drive/folders/1nYyaQXOBjNdUJDsmJpcRpu6oE55aQoLA) and save it in pretrained folder
1.  ```console
    sudo docker build .
    ```

### Run docker

1.  ```console
    sudo docker run -it --rm --runtime nvidia --gpus all -v /home/vision:/home <IMAGE ID>
    ```

#### Docker commends

1.  All images
    ```console
    sudo docker images
    ```
1.  Running containers
    ```console
    sudo docker ps
    ```
1.  All containers
    ```console
    sudo docker ps -a
    ```
1.  Clean up
    ```console
    sudo docker system prune
    ```
1.  Clean up
    ```console
    sudo docker system prune -a
    ```

python3 detect.py --source "../input/trash.jpg" --weights "../detection_weights.pt" --img-size 640 --conf 0.675 --exist-ok --project ../ --name output

Miniforge3-Linux-x86_64

https://github.com/conda-forge/miniforge/releases
