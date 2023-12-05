from sanic import Sanic,Request,Blueprint
from sanic.response import text,json
from sanic.log import logger
from sanic_ext import Extend
from paddleocr import PaddleOCR, draw_ocr, download_with_progressbar


app = Sanic(name="OCR")
# 配置
app.config.OAS_UI_REDOC = True
app.config.OAS_UI_SWAGGER = False
# 扩展, 在配置后面
Extend(app)


@app.route("/api/ocr")
async def ocr_request(request):
    """ocr接口
    Auto-documentation
    https://sanic.dev/en/plugins/sanic-ext/openapi/autodoc.html#summary-and-description

    openapi:
    ---
    operationId: ocr_request
    tags:
      - api
    parameters:
      - name: img
        in: query
        description: img url
        required: false
    """
    if request.args.get("img"):
        logger.info(request.args.get("img"))
    if request.json and request.json["img"]:
        logger.info(request.json["img"])
    if request.form.get("img"):
        logger.info(request.form.get("img"))
    file = request.files.get('file') # 如果支持上传多个request.files.getlist('file')
    if file:
        logger.info(file.name)
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    result = ocr.ocr("./imgs/11.jpg", cls=True)
    return json(result)

@app.get("/")
async def hello_world(request):
    logger.info('Here is your log')
    return text("Hello, world1.")


# CLI:sanic path.to.server:app --single-process
# --single-process等价于single_process=True
# sanic server:app or sanic server or sanic server.app --debug --auto-reload
if __name__ == "__main__":
    app.run(debug=False, auto_reload=True)
    # host: 监听的IP, port: 监听的端口(默认8000), auto_reload: 修改代码之后是否自动重启
    # debug=False, access_log=False
    # app.run(host="127.0.0.1", port=8888,auto_reload=True)