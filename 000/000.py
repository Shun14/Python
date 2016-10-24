#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    #use a truetype font
    font = ImageFont.truetype(r'C:/windows/fonts/Arial.ttf', size=50)
    fillcolor = "#ff0000"
    width, height = img.size
    
    draw.text((width-50, 0),'99', font=font,fill=fillcolor)
    img.save(r'D:\reset.jpg','jpeg')
    return 0
if __name__ == '__main__'  :
    
    img = Image.open(r'E:\desktop_pic\1.jpg')
    add_num(img)
    
    