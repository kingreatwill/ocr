FROM python:3.10.0-bullseye

RUN apt-get update && apt-get install -y libgl1
# yum install mesa-libGL -y
RUN pip install --upgrade pip
RUN pip install paddlepaddle==2.5.2 "paddleocr>=2.6.0.3"

WORKDIR /code
COPY . .
CMD ["python", "ocr_img_demo.py"]