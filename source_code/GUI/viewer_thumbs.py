"""
欲实现图像处理前后的预览
因较为麻烦暂且搁置
"""

import os, sys, math
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL.ImageTk import PhotoImage


def make_thumb(img_direction, size=(100, 100)):
    """
    在内存中创建缩略图，用于显示

    """
    try:
        img_object = Image.open(img_direction)
        img_object.thumbnail(size, Image.ANTIALIAS)
        return img_object
    except:
        print("Can't make thumb, skip:", img_direction)


class ViewWidget(Toplevel):
    def __init__(self, img_direction, img_file):
        Toplevel.__init__(self)
        self.title(img_file)
        img_path = os.path.join(img_direction, img_file)

        img_object = PhotoImage(file=img_path)
        ttk.Label(self, image=img_object).grid()
        self.savephoto = img_object


def viewer(img_direction, kind=Toplevel, cols=None):
    win = kind()
    win.title('Viewer:' + img_direction)
    quit = ttk.Button(win, text='QUIT', command=win.quit(), bg='beige')
    quit.pack(fill=X, side=BOTTOM)
    thumb = make_thumb(img_direction)
    if not cols:
        cols = int(math.ceil(math.sqrt(len(thumb))))

