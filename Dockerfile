# Start FROM Nvidia PyTorch image https://ngc.nvidia.com/catalog/containers/nvidia:pytorch
# FROM nvcr.io/nvidia/pytorch:21.02-py3
# FROM nvcr.io/nvidia/l4t-pytorch:r32.5.0-pth1.7-py3
FROM nvcr.io/nvidia/dli/dli-nano-ai:v2.0.1-r32.5.0


# download pretrained  model

# Install linux packages
RUN apt update && apt install -y zip screen libgl1-mesa-glx
# RUN apt install -y curl
# RUN curl -O https://github.com/Archiconda/build-tools/releases/download/0.2.3/Archiconda3-0.2.3-Linux-aarch64.sh
# COPY Archiconda3-0.2.3-Linux-aarch64.sh .
RUN apt -y wget 
RUN wget https://github.com/Archiconda/build-tools/releases/download/0.2.3/Archiconda3-0.2.3-Linux-aarch64.sh
RUN chmod +x Archiconda3-0.2.3-Linux-aarch64.sh
RUN yes yes | ./Archiconda3-0.2.3-Linux-aarch64.sh
# Install python dependencies
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt gsutil 
#RUN pip3 install --no-cache -r requirements.txt gsutil notebook

RUN mkdir -p /vision
# ADD https://drive.google.com/u/0/uc?id=1lvyZZbC9NLcS8a__YPcUP7rDiIpbRpoF&export=download /vision/pretrained/
# Create working directory
WORKDIR /vision

# Copy contents
COPY . /vision

RUN git clone https://github.com/shariqfarooq123/AdaBins.git 
RUN git clone https://github.com/ultralytics/yolov5.git


# Set environment variables
ENV HOME=/vision

# Copy weights
#RUN python3 -c "from models import *; \
#attempt_download('weights/yolov5s.pt'); \
#attempt_download('weights/yolov5m.pt'); \
#attempt_download('weights/yolov5l.pt')"


# ---------------------------------------------------  Extras Below  ---------------------------------------------------

# Build and Push
# t=ultralytics/yolov5:latest && sudo docker build -t $t . && sudo docker push $t
# for v in {300..303}; do t=ultralytics/coco:v$v && sudo docker build -t $t . && sudo docker push $t; done

# Pull and Run
# t=ultralytics/yolov5:latest && sudo docker pull $t && sudo docker run -it --ipc=host --gpus all $t

# Pull and Run with local directory access
# t=ultralytics/yolov5:latest && sudo docker pull $t && sudo docker run -it --ipc=host --gpus all -v "$(pwd)"/coco:/usr/src/coco $t

# Kill all
# sudo docker kill $(sudo docker ps -q)

# Kill all image-based
# sudo docker kill $(sudo docker ps -qa --filter ancestor=ultralytics/yolov5:latest)

# Bash into running container
# sudo docker exec -it 5a9b5863d93d bash

# Bash into stopped container
# id=$(sudo docker ps -qa) && sudo docker start $id && sudo docker exec -it $id bash

# Send weights to GCP
# python -c "from utils.general import ; strip_optimizer('runs/train/exp0_*/weights/best.pt', 'tmp.pt')" && gsutil cp tmp.pt gs://.pt

# Clean up
# docker system prune -a --volumes