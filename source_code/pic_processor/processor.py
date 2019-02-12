# -*- coding:UTF-8 -*-
import os, sys
from PIL import Image

# pictureDir = input("please input the direction of the picture")  需要在实现ui时进行改动


def process(picture_direction1, picture_direction2, output_direction):
    with Image.open(picture_direction1).convert("L") as im1:
        with Image.open(picture_direction2).convert("L") as im2:
            # 生成一张大小容纳两张照片，底色白色半透明的底图
            output_width = max(im1.size[0], im2.size[0])
            mid_width = min(im1.size[0], im2.size[0])
            output_height = max(im1.size[1], im2.size[1])
            mid_height = min(im1.size[1], im2.size[1])
            output = Image.new("RGBA", (output_width, output_height),
                               (255, 255, 255, 128))
            # 获取像素点颜色……

            for m in range(0, output_height):
                for n in range(0, output_width):
                    if m <= mid_height - 1 and n <= mid_width - 1:
                        if (m + n) % 2 == 0:
                            colour = im1.getpixel((n, m))
                            output.putpixel((n, m), (0, 0, 0, colour))
                        else:
                            colour = im2.getpixel((n, m))
                            output.putpixel((n, m), (255, 255, 255, colour))
                    elif m >= mid_height and n < mid_width:
                        if im1.size[1] > im2.size[1]:
                            output.putpixel((n, m), im1.getpixel((n, m)))
                        else:
                            output.putpixel((n, m), im2.getpixel((n, m)))
                    elif m < mid_height and n >= mid_width:
                        if im1.size[0] > im2.size[0]:
                            output.putpixel((n, m), im1.getpixel((n, m)))
                        else:
                            output.putpixel((n, m), im2.getpixel((n, m)))
            # 存储
            output.save(os.path.splitext(output_direction)[0] + ".png", "PNG")


def make_thumbs(img_direction, size=(100, 100)):
    if img_direction != "":
        img_object = Image.open(img_direction)
        img_object.thumbnail(size, Image.ANTIALIAS)
        return img_object

