# ocr


## 安装
https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_ch/quickstart.md

https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/ppstructure/docs/quickstart.md

https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_ch/whl.md

[模型下载地址](https://gitee.com/paddlepaddle/PaddleOCR/blob/dygraph/doc/doc_ch/models_list.md)

### 安装PaddlePaddle

https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/linux-pip.html

`python -m pip install paddlepaddle==2.5.2`
```
python3 -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
python -m pip install paddlepaddle==2.5.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
```
### 安装PaddleOCR whl包
`pip install "paddleocr>=2.6.0.3" # 推荐使用2.0.1+版本`

```
# 安装 paddleocr，推荐使用2.6版本
pip3 install "paddleocr>=2.6.0.3"

# 安装 图像方向分类依赖包paddleclas（如不需要图像方向分类功能，可跳过）
pip3 install paddleclas>=2.4.3
```

### dockerfile
```
FROM python:3.10.0-bullseye

# ENV PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --upgrade pip
RUN pip install paddlepaddle==2.5.2 "paddleocr>=2.6.0.3"

WORKDIR /code

COPY docs ./build/docs
COPY overrides ./build/overrides
COPY mkdocs.yml ./mkdocs.yml

RUN mkdocs build

EXPOSE 8000

CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]
```

### 参数说明
https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_ch/whl.md#6-%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E


