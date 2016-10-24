#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    #use a truetype font
    font = ImageFont.truetype(r'C:/windows/fonts/Arial.ttf', size=50)
    fillcolor = "#ff0000"
    width, height = img.size
    To_addr = input("请输入存储路径：\n")
    draw.text((width-100, 0),'99+', font=font,fill=fillcolor)
    img.save(To_addr,'jpeg')
    return 0
if __name__ == '__main__'  :
    addr = input("请输入需要修改的图片路径：\n")
    img = Image.open(addr)
    add_num(img)
    
    