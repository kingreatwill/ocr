from paddleocr import PaddleOCR, draw_ocr, download_with_progressbar

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
img_path = './imgs/11.jpg' # 可以是网络图片地址或者PDF
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

# 显示结果
from PIL import Image
result = result[0]
# 如果是网络图片
# download_with_progressbar(img_path, 'tmp.jpg')
# img_path
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('./imgs/result.jpg')

# 输出结果(如果是pdf则是是多个list)
"""
[[[28.0, 37.0], [302.0, 39.0], [302.0, 72.0], [27.0, 70.0]], ('纯臻营养护发素', 0.9978386163711548)]
[[[26.0, 83.0], [173.0, 83.0], [173.0, 104.0], [26.0, 104.0]], ('产品信息/参数', 0.9898311495780945)]
"""
# 可以转换成json格式,一个list
"""
[{
        "BoxPoints":[
            {
                "X":26,
                "Y":37
            },
            {
                "X":303,
                "Y":37
            },
            {
                "X":303,
                "Y":73
            },
            {
                "X":26,
                "Y":73
            }
        ],
        "Score":0.9965136647224426,
        "Text":"纯臻营养护发素"
    }]
"""