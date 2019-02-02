# -*- coding:UTF-8 -*-
import os, sys
from PIL import Image

# pictureDir = input("please input the direction of the picture") # 需要在实现ui时进行改动


def process(picture_direction1, picture_direction2, output_direction):
    with Image.open(picture_direction1) as im1:
        with Image.open(picture_direction2) as im2:
            output = Image.new("RGBA", (max(im1.size[0], im2.size[0]), max(im1.size[1], im2.size[1])),
                               (255, 255, 255, 50))
            # 处理模块


            output.save(os.path.splitext(output_direction)[0] + ".png", "PNG")


def test_function():
    print("test")

