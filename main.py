

import requests
import re
from urllib import parse
import os
from tkinter import *
from PIL import ImageTk, Image


class BingImageSpider(object):
    def __init__(self):
        self.url = "http://cn.bing.com/images/async?q={0}&first={1}&count=35&relp=35&lostate=r&mmasync=1&dgState=x*175_y*848_h*199_c*1_i*106_r*0"
        self.headers = {'User-Agent': 'Mozilla/4.0'}

    def save_image(self, link, filename):
        html = requests.get(url=link, headers=self.headers).content
        with open(filename, 'wb') as fut:
            fut.write(html)

    def get_image(self, url, word, i, m):
        res = requests.get(url=url, headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        pattern = re.compile('<div class="img_cont hoff".*?<img class="mimg".*?src="(.*?)".*?</div>', re.S)
        list_ = pattern.findall(html)
        directory = 'C:/Users/{}/Desktop/image/{}/'.format(os.environ['username'], word)
        if os.path.exists(directory):
            pass
        else:
            os.makedirs(directory)

        for link in list_:
            filename = '{}{}_{}.jpg'.format(directory, word, i)

            self.save_image(link, filename)
            i += 1

    def run(self, word, m):
        word_parse = parse.quote(word)
        for j in range(m):
            url = self.url.format(word_parse, 1 + j * 35)
            self.get_image(url, word, 1 + j * 35, m)


def work():
    m = int(p.get())
    if m == 0:
        m = 1
    spider.run(k.get(), m)

if __name__ == '__main__':
    spider = BingImageSpider()
    root = Tk()
    root.title("混氏新子BING图片批量下载器")
    root.geometry("1088x626+300+0")
    root.resizable(0, 0)
    photo = PhotoImage(file='main.gif')
    w = Label(root, image=photo)
    w.pack()
    ent = Entry(root)
    ent.pack()
    ent.focus_set()
    k = Entry(root, width=20)
    k.place(x=500, y=450)
    k1 = Label(root, text='搜索内容', bg='DeepSkyBlue')
    k1.place(x=420, y=450)
    p = Entry(root, width=5)
    p.place(x=520, y=500)
    p1 = Label(root, text='几个35张照片？', bg='DeepSkyBlue')
    p1.place(x=420, y=500)
    t = Button(root, text="点我下载", command=work)
    t.place(x=500, y=320, width=100, height=100)
    root.mainloop()
