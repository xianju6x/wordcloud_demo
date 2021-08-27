#!/usr/bin/env python3

import os
import random
from wordcloud import WordCloud
from PIL import Image


def gen_txt(source):
    
    whole = []
    for w in source:
        temp = []
        for _ in range(random.randint(1,5)):
            temp.append(w)
        whole.extend(temp)
    random.shuffle(whole)
    text = ' '.join(whole)
    return text


def gen_png(text,out_png):
    
    d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    wordcloud = WordCloud().generate(text)
    wordcloud = WordCloud(width=600,height=800,max_words=100,font_step=1,repeat=True,contour_width=3).generate(text)
    wordcloud.to_file(os.path.join(d, out_png))


if __name__ == '__main__':
    
    out_png = 'wordcloud.png'
    source = ['Hello','Ciao','Привет','Bonjour','γειασας','Hallo']
    text = gen_txt(source)
    gen_png(text,out_png)
    img = Image.open(out_png)
    img.show()
