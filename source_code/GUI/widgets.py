import os, sys
from PIL import Image
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from source_code.pic_processor import processor


# 用于打开文件的选择对话框
class OpenFileFrame(ttk.Frame):
    # 初始化，默认文本框空白
    def __init__(self, parent=None, text=''):
        ttk.Frame.__init__(self, parent)
        self.make_widgets()

    def make_widgets(self):
        # 一个text区域用于输入文件路径
        text = Text(self, width=60, height=1)
        text.grid(column=0, row=0)
        # 一个button用于可视化的选取文件
        ttk.Button(self, text='...', width=3, command=self.open_file).grid(column=1, row=0)
        self.text = text

    def open_file(self):
        # button执行的函数
        file = filedialog.askopenfilename(filetypes=processor.image_type)
        if file:
            # 将路径显示在text区域以便使用者确定
            self.text.delete('1.0', END)
            self.text.insert('1.0', file)
            self.text.mark_set(INSERT, '1.0')
            self.text.focus()

    # 获取文本框中内容
    def get_file(self):
        return self.text.get('1.0', END + '-1c')


def open_pic(direction):
    direction = filedialog.askopenfile()
    return direction
