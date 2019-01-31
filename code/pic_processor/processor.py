# -*- coding:UTF-8 -*-

from PIL import Image

# pictureDir = input("please input the direction of the picture") # 需要在实现ui时进行改动


def process(picture_direction):
    original_picture1 = Image.open(picture_direction)

