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
root.iconbitmap("..\\pp_ico.ico")

option_pages = ttk.Notebook(root)
# 标签页的声明
convert_frame = ttk.Frame(option_pages)
option_pages.add(convert_frame, text='格式转换')

phantom_tank_frame = ttk.Frame(option_pages)
option_pages.add(phantom_tank_frame, text='幻影坦克')

option_pages.grid(column=0, row=0)

# 格式转换标签页

img_type = StringVar()
# 文件选取
ttk.Label(convert_frame, text='待转换文件：').grid(column=0, row=0, padx=5, pady=5)
to_convert = widgets.OpenFileFrame(convert_frame)
to_convert.grid(column=1, row=0, columnspan=3)
ttk.Label(convert_frame, text='目标格式：').grid(column=0, row=1, padx=5, pady=5)
# 格式选取列表
type_list = ttk.Combobox(convert_frame, textvariable=img_type, state='readonly')
type_list['values'] = processor.output_image_type_name
type_list.grid(column=1, row=1, sticky=W)


def img_convert():
    try:
        original_image = to_convert.get_file()
        output_image = filedialog.asksaveasfilename(filetypes=[('图片', '.*')])
        if output_image:
            image = Image.open(original_image)
            image.save(os.path.splitext(output_image)[0] + '.' + type_list.get())
    except ValueError:
        pass


convert_button = ttk.Button(convert_frame, text='转换', command=img_convert)
convert_button.grid(column=2, row=1, sticky=W)

# 幻影坦克标签页

ttk.Label(phantom_tank_frame, text="表图地址").grid(column=0, row=0, padx=5, pady=5, sticky=W)
off1 = widgets.OpenFileFrame(phantom_tank_frame)
off1.grid(column=1, row=0)
ttk.Label(phantom_tank_frame, text="里图地址").grid(column=0, row=1, padx=5, pady=5, sticky=W)
off2 = widgets.OpenFileFrame(phantom_tank_frame)
off2.grid(column=1, row=1)


def pic_process(*args):
    try:
        picture1 = off1.get_file()
        picture2 = off2.get_file()
        output_path = filedialog.asksaveasfilename(filetypes=[("PNG", ".png")])
        if output_path:
            processor.process(picture1, picture2, output_path)
    except ValueError:
        pass


process = ttk.Button(phantom_tank_frame, text="生成幻影坦克", command=pic_process)
process.grid(column=1, row=2, pady=20, sticky=(N, W, E))

root.mainloop()
