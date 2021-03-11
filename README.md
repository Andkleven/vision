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
    sudo docker run -it --rm --runtime nvidia --gpus all -v /home/vision:/home ID
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
