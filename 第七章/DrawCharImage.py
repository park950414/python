# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 21:36:10 2017

@author: park
"""
from PIL import Image
ascii_char=list(',./<>?;:"[]{}-=_+!@#$%^&*()~~qwertyuioQWERTYUIOPASDFGHJKLZXCVBNM')
def get_char(r,g,b,alpha=256):
    if alpha==0:
        return ' '
    gray=int(0.2126*r+0.7152*g+0.0722*b)
    unit =int(256/len(ascii_char))
    return ascii_char[gray//unit]

def main():
    im=Image.open("astro.png")
    WIDTH,HEIGHT=250,60
    im=im.resize((WIDTH,HEIGHT))
    txt=''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt +=get_char(*im.getpixel((j,i)))
        txt +='\n'
    fo=open("pic_char.txt","w")
    fo.write(txt)
    fo.close()
main()