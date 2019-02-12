# 未写完GUI部分

# 应考虑重构组件的声明

import os, sys, math
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from source_code.GUI import widgets
from source_code.GUI import viewer_thumbs
from PIL import Image
from PIL.ImageTk import PhotoImage
from source_code.pic_processor import processor

root = Tk()
root.title("图片处理小工具")

option_pages = ttk.Notebook(root)
# 标签页的声明
phantom_tank_frame = ttk.Frame(option_pages)
option_pages.add(phantom_tank_frame, text='幻影坦克')

test_frame = ttk.Frame(option_pages)
option_pages.add(test_frame, text='test')

option_pages.grid(column=0, row=0)

# 幻影坦克标签页

ttk.Label(phantom_tank_frame, text="图片一地址").grid(column=0, row=0, padx=5, pady=5, sticky=W)
off1 = widgets.OpenFileFrame(phantom_tank_frame)
off1.grid(column=1, row=0)
ttk.Label(phantom_tank_frame, text="图片二地址").grid(column=0, row=1, padx=5, pady=5, sticky=W)
off2 = widgets.OpenFileFrame(phantom_tank_frame)
off2.grid(column=1, row=1)
'''
ttk.Label(phantom_tank_frame, text="输出图地址").grid(column=0, row=2, padx=5, pady=5, sticky=W)
sff = widgets.SaveFileFrame(phantom_tank_frame)
sff.grid(column=1, row=2)
'''


def pic_process(*args):
    try:
        picture1 = off1.get_file()
        picture2 = off2.get_file()
        print(picture1)
        output_path = filedialog.asksaveasfilename(filetypes=[("PNG", ".png")])
        processor.process(picture1, picture2, output_path)
    except ValueError:
        pass


process = ttk.Button(phantom_tank_frame, text="生成幻影坦克", command=pic_process)
process.grid(column=1, row=2, pady=20, sticky=(N, W, E))
#pic1_view = ttk.LabelFrame(test_frame, text="预览")
#pic1_view.grid(column=0, row=0)
pic = Label(test_frame)

pic.grid()

root.mainloop()
