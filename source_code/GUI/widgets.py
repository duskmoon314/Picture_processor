import os, sys
from PIL import Image
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from source_code.pic_processor import processor


class OpenFileFrame(ttk.Frame):
    def __init__(self, parent=None, text=''):
        ttk.Frame.__init__(self, parent)
        self.make_widgets()

    def make_widgets(self):
        text = Text(self, width=50, height=1)
        text.grid(column=0, row=0)
        ttk.Button(self, text='...', width=3, command=self.open_file).grid(column=1, row=0)
        self.text = text

    def open_file(self):
        file = filedialog.askopenfilename()
        if file:
            self.text.delete('1.0', END)
            self.text.insert('1.0', file)
            self.text.mark_set(INSERT, '1.0')
            self.text.focus()

    def get_file(self):
        return self.text.get('1.0', END + '-1c')


class SaveFileFrame(ttk.Frame):
    def __init__(self, parent=None, text='', pic1='', pic2=''):
        ttk.Frame.__init__(self, parent)
        self.make_widgets()

    def make_widgets(self):
        text = Text(self, width=50, height=1)
        text.grid(column=0, row=0)
        ttk.Button(self, text='...', width=3, command=self.save_file()).grid(column=1, row=0)
        self.text = text

    def save_file(self):
        file = filedialog.asksaveasfilename()
        if file:
            # processor.process(pic1, pic2, file)
            self.text.delete('1.0', END)
            self.text.insert('1.0', "已输出为" + file)
            self.text.mark_set(INSERT, '1.0')
            self.text.focus()

    def get_file(self):
        print(self.text)
        print("\n")


def open_pic(direction):
    direction = filedialog.askopenfile()
    return direction
