from sanic import Sanic,Request,Blueprint
from sanic.response import text,json
from sanic.log import logger
from sanic_ext import Extend
from paddleocr import PaddleOCR, draw_ocr, download_with_progressbar

ocr = PaddleOCR(use_angle_cls=True, lang="ch")

app = Sanic(name="OCR")
# 配置
app.config.OAS_UI_REDOC = True
app.config.OAS_UI_SWAGGER = False
# 扩展, 在配置后面
Extend(app)

api = Blueprint("api", url_prefix="/api")
app.blueprint(api)

@api.post("/ocr")
async def ocr_request(request):
    logger.info(request.json)
    result = ocr.ocr("./imgs/11.jpg", cls=True)
    return json(result)

@app.get("/")
async def hello_world(request):
    logger.info('Here is your log')
    return text("Hello, world1.")


# CLI:sanic path.to.server:app --single-process
# --single-process等价于single_process=True
# sanic server:app or sanic server
if __name__ == "__main__":
    app.run(auto_reload=True)
    # host: 监听的IP, port: 监听的端口(默认8000), auto_reload: 修改代码之后是否自动重启
    # debug=False, access_log=False
    # app.run(host="127.0.0.1", port=8888,auto_reload=True)