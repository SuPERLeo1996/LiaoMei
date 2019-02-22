from PIL import Image


def getText(img):
    img = img.convert("L")  # 转为灰度图片
    charlist = ''
    for h in range(0, img.size[1]):
        for w in range(0, img.size[0]):
            gray = img.getpixel((w, h))  # 返回像素值，介于0-255之间256个
            pos = gray / 256
            charlist = charlist + codelist[int((count - 1) * pos)]  # 这里count-1是因为字符串索引是从0开始
        charlist = charlist + '\r\n'  # 不同系统对应的换行符不一样\n-windows \r-Linux
    return charlist


def getImage():
    # 取得图像
    file = open(r"C:\Users\Leo\Desktop\123.jpg", 'rb')
    img = Image.open(file)
    return img


def trantxt():
    # 输出到文本中去
    outfile = open('tmp.txt', 'w')
    outfile.write(getText(img))
    outfile.close()


if __name__ == '__main__':
    img = getImage()
    width, height = img.size[0], img.size[1]  # 0-width，1-height
    codelist = """qwertyuiop[]asdfghjkl;'zxcvbnm,./`~!@#$%^&<()*+{}:"?> |""" 
    count = len(codelist)
    scale = width / height  # 宽度与高度的比例，为了维护图像比例不要失真
    img = img.resize((int(width * 0.2), int(width * 0.1 / scale)))  # 这里的0.1可以改成你喜欢的比例
    trantxt()