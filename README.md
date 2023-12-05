# ocr
## web框架
https://sanic.dev/zh/guide/getting-started.html#%E5%AE%89%E8%A3%85-install

```
pip install sanic==23.6.0 sanic-ext==23.6.0
```
> redoc:http://localhost:8000/docs {/redoc} or swagger: http://localhost:8000/docs/swagger
> swagger配置: https://sanic.dev/zh/plugins/sanic-ext/openapi/ui.html#%E9%85%8D%E7%BD%AE%E9%80%89%E9%A1%B9-config-options

### 上传文件
1. 上传文件
```
@app.route("/upload", methods=['POST'])
async def upload(request):
    allow_type = ['.jpg', '.png', '.gif'] # 允许上传的类型
    file = request.files.get('file')
    type = os.path.splitext(file.name)

    if type[1] not in allow_type:
        return json({"code": -1, "msg": "只允许上传.jpg.png.gif类型文件"})

    name = str(uuid4())+type[1]
    path = "/user/data/web/upload" # 这里注意path是绝对路径

    async with aiofiles.open(path+"/"+name, 'wb') as f:
        await f.write(file.body)
    f.close()
    return json({"code": 0, "msg": "上传成功", "data": {
        "name": name,
        "url": "/upload/"+name
    }})
```

### 输出文件
1. [输出文件](https://sanic.dev/zh/guide/advanced/streaming.html#%E6%96%87%E4%BB%B6%E6%B5%81-file-streaming)

2. 输出静态文件,这就需要用到 Sanic 静态文件代理
```
path = "/user/data/web/upload" # 这里注意path是绝对路径
app.static("/upload", path)
```
### 其它
> 进阶 [Worker 管理器 | Sanic 框架](https://zhuanlan.zhihu.com/p/571588906)
> [Worker Manager](https://sanic.dev/en/guide/deployment/manager.html#how-sanic-server-starts-processes)

## 安装
https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_ch/quickstart.md

https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/ppstructure/docs/quickstart.md

https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_ch/whl.md



### 模型
不指定模型目录,自动下载
```
download https://paddleocr.bj.bcebos.com/PP-OCRv4/chinese/ch_PP-OCRv4_det_infer.tar to /root/.paddleocr/whl/det/ch/ch_PP-OCRv4_det_infer/ch_PP-OCRv4_det_infer.tar
download https://paddleocr.bj.bcebos.com/PP-OCRv4/chinese/ch_PP-OCRv4_rec_infer.tar to /root/.paddleocr/whl/rec/ch/ch_PP-OCRv4_rec_infer/ch_PP-OCRv4_rec_infer.tar
download https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_cls_infer.tar to /root/.paddleocr/whl/cls/ch_ppocr_mobile_v2.0_cls_infer/ch_ppocr_mobile_v2.0_cls_infer.tar
```


[模型下载地址](https://gitee.com/paddlepaddle/PaddleOCR/blob/dygraph/doc/doc_ch/models_list.md)

server 模型下载地址:
https://paddleocr.bj.bcebos.com/PP-OCRv4/chinese/ch_PP-OCRv4_det_server_infer.tar
https://paddleocr.bj.bcebos.com/PP-OCRv4/chinese/ch_PP-OCRv4_rec_server_infer.tar
https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_cls_slim_infer.tar

如果指定了rec_model_dir,需要指定识别模型字典路径: rec_char_dict_path,如:"./ppocr/utils/ppocr_keys_v1.txt"
https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/ppocr/utils/ppocr_keys_v1.txt

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


### 获取access_token
https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application
```
# 获取access_token，替换下列示例中的API Key与Secret Key
curl 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=xx&client_secret=xx'
```

### 车牌识别
https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/applications/%E8%BD%BB%E9%87%8F%E7%BA%A7%E8%BD%A6%E7%89%8C%E8%AF%86%E5%88%AB.md

[数据集](https://aistudio.baidu.com/datasetdetail/101595) 的 [文件名规则说明](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/applications/%E8%BD%BB%E9%87%8F%E7%BA%A7%E8%BD%A6%E7%89%8C%E8%AF%86%E5%88%AB.md#31-%E6%95%B0%E6%8D%AE%E9%9B%86%E6%A0%87%E6%B3%A8%E8%A7%84%E5%88%99)
