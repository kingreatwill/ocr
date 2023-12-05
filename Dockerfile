FROM python:3.10.0-bullseye

RUN apt-get update && apt-get install -y libgl1
# yum install mesa-libGL -y
RUN pip install --upgrade pip
RUN pip install sanic==23.6.0 sanic-ext==23.6.0 paddlepaddle==2.5.2 "paddleocr>=2.6.0.3"

WORKDIR /code
COPY . .
ENTRYPOINT ["sanic", "server:app"]

# docker build -t ocr:v0.01 .
# docker run -it --rm -p 8000:8000 --name ocr ocr:v0.01 --debug