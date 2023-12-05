FROM python:3.10.0-bullseye

RUN apt-get update && apt-get install -y libgl1
# yum install mesa-libGL -y
RUN pip install --upgrade pip
RUN pip install sanic==23.6.0 sanic-ext==23.6.0 paddlepaddle==2.5.2 "paddleocr>=2.6.0.3"
