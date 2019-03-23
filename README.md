# Picture Processor

## 当前版本：1.1

### Github文件目录

README.md: 用户文档等内容

souce_code: 源代码

venv: python虚拟环境

README_img: README.md中用到的图片

pp_ico.ICO: 图标文件（实际上源代码中用的是二进制编码的格式，仅放在此处作为格式转换的又一个例子）

.idea: 一些配置信息（懒得删了）

.gitattributes LICENSE: git配置与许可

### 功能：

- 简单的格式转换，支持大部分常见图片格式。可以转换至其他文件夹并重命名。

![格式转换](https://github.com/duskmoon314/Picture_processor/blob/master/README_img/%E6%A0%BC%E5%BC%8F%E8%BD%AC%E6%8D%A2.png?raw=true)

例子：原图 [Kaitan](https://www.pixiv.net/member.php?id=2924751) 的 [after](https://www.pixiv.net/member_illust.php?mode=medium&illust_id=55348597)

原图jpg

![原图jpg](https://github.com/duskmoon314/Picture_processor/blob/master/README_img/example.jpg?raw=true)

生成的png

![PNG](https://github.com/duskmoon314/Picture_processor/blob/master/README_img/example.PNG?raw=true)

生成的gif

![GIF](https://github.com/duskmoon314/Picture_processor/blob/master/README_img/example.GIF?raw=true)

生成的bmp

![BMP](https://raw.githubusercontent.com/duskmoon314/Picture_processor/master/README_img/example.BMP)

- 生成“幻影坦克”，即用白色/黑色作为背景时显示不同图像的png文件。原理利用点阵故效果不能算是很理想

![幻影坦克](https://github.com/duskmoon314/Picture_processor/blob/master/README_img/%E5%B9%BB%E5%BD%B1%E5%9D%A6%E5%85%8B.png?raw=true)

例子：原图 [Kaitan](https://www.pixiv.net/member.php?id=2924751) 的 [after](https://www.pixiv.net/member_illust.php?mode=medium&illust_id=55348597) 和 [公国と200年の夜](https://www.pixiv.net/member_illust.php?mode=medium&illust_id=60565407)

生成的图片

![生成图](https://github.com/duskmoon314/Picture_processor/blob/master/README_img/output.png?raw=true)

白色为底的显示效果

![白色底](https://github.com/duskmoon314/Picture_processor/blob/master/README_img/output_whiteBackGround.png?raw=true)

黑色为底的显示效果

![黑色底](https://github.com/duskmoon314/Picture_processor/blob/master/README_img/output_blackBackGround.png?raw=true)



## 未来暂定目标：

- 加入图片加隐水印（通过傅里叶变换转为频域的方法）
- 加入GIF生成
- 加入图片选择后的缩略图预览效果
- 加入基于MIT License的waifu2x技术进行动漫类型图片的放大

## License等

请自由修改，然后pull request

XD

若有需求，可以在Issues写



## p.s.

对于Git和GitHub的使用还不是很熟，可能有多余无用的文件也在库里。请注意



###### 贡献者

Campbell He (duskmoon314)