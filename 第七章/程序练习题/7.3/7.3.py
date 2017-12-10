# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 13:39:43 2017

@author: park
"""

from PIL import Image
ascii_char = list('一二三丁人入大工连理国家健康繁荣')
def get_char(r,g,b,alpha=256):
    if alpha=='0':
        return' '
    gray=int(0*2126*r+0.7152*g+0.0722*b)
    unit=256/len(ascii_char)
    return ascii_char[int(gray//unit)]
def main():
    im=Image.open("astro.png")
    WIDTH=200
    HEIGHT=60
    im=im.resize((WIDTH,HEIGHT))
    txt=''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt+=get_char(*im.getpixel((j,i)))
        txt+='\n'
    fo=open("pic_char.txt","w")
    fo.write(txt)
    fo.close()
    
main()
        