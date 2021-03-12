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
    docker system prune
    ```
1.  Clean up
    ```console
    docker system prune -a
    ```

python3 detect.py --source "input/trash.jpg" --weights "detection_weights.pt" --img-size 640 --conf 0.675 --exist-ok --name output
