# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 11:13:20 2017

@author: ondrej
"""

from PIL import Image, ImageFont, ImageDraw
from os import walk
from datetime import datetime

f = []
for (dirpath, dirnames, filenames) in walk('/Users/ondrej/Desktop/Orchidey_day'):
    f.extend(filenames)
    break

im=Image.open(dirpath+'/'+f[1])
date_start = im._getexif()[36867]
date_format="%Y:%m:%d %X"
d_start = datetime.strptime(date_start,date_format)

font=ImageFont.truetype("/Library/Fonts/Arial.ttf",50)
dir_name = "Label/"
for fim in f:
    if '.jpg' in fim:
        im=Image.open(dirpath+'/'+fim)
        im_date = im._getexif()[36867]
        d = datetime.strptime(im_date,date_format)
        delta = (d - d_start).days
        draw = ImageDraw.Draw(im)
        draw.text((0,0),"Day %g"%delta,(255,255,255),font=font)
        im.save(dir_name+'day_'+fim)