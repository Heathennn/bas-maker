# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image
from functools import reduce
# 灰度值 0 - 255 黑 0 - > 白255
# 一个文字大小默认为10x10
font_width = 10
font_height = 10
# 文字颗粒度 10
font_unit = 10
# 默认有几种颜色
font_color_number = 2
# (变量名, 内容, x, y, color, 变量名, 秒数)
bas_template = '''def text %s {
 content = "%s"
 fontSize = 10
 x = %s
 y = %s
 color = %s
}
set %s {} %ss
'''
def rgb_to_hex(r, g, b):
  return ('{:02X}' * 3).format(r, g, b)

def get_font_color(gray_value, number=font_color_number):
    print('111')

def convertImg():
    img = Image.open('./images/xiaozhan.jpg')
    img = img.convert("L")
    # value = get_gray_value(img)
    width_total = img.width // font_unit
    height_total = img.height // font_unit
    print('图片高为: %spx, 宽为: %spx' % (img.height, img.width))
    print('单字大小为: %apx' % font_unit)
    print('字数为: %a x %a' % (width_total, height_total))
    print('生成代码中...')
    bas_result = ''
    for h in range(height_total):
        for w in range(width_total):
            print('正在打印第%a行第%a个字' % (h, w))
            left = font_unit * w
            right = font_unit * (w + 1)
            top = font_unit * h
            bottom = font_unit * (h + 1)
            box = (left, top, right, bottom)
            crop_box = img.crop(box)
            print('灰度值:%a' % get_gray_value(crop_box))
            print('HEX色值: %a' % rgb_to_hex(get_gray_value(crop_box), get_gray_value(crop_box), get_gray_value(crop_box)))
            color = '0x%s' % rgb_to_hex(get_gray_value(crop_box), get_gray_value(crop_box), get_gray_value(crop_box))
            text_code = bas_template % ('bas%s%s' % (h, w), '战', left, top, color, 'bas%s%s' % (h, w), 5)
            bas_result += text_code + '\n'

    f = open('bas.text', 'w+', encoding='utf-8')
    print(bas_result)
    f.write(bas_result)
    f.close()

    print('=== 处理完毕 ===')
def setTextForImage(img):
    print('111')

def get_gray_value(img):
    return reduce(lambda x, y: x + y, img.getdata()) // (img.size[0] * img.size[1])
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    convertImg()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
