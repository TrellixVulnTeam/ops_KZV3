#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: rongguo
@license: Apache Licence 
@contact: rongo.wei@gmail.com
@software: PyCharm
@project: oms
@file: common.py
@time: 17-5-15 下午2:45
"""

import os, sys, time, re
import subprocess
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

from ops.settings import BASE_DIR


# def chown(path, user, group=''):
#     if not group:
#         group = user
#     try:
#         uid = pwd.getpwnam(user).pw_uid
#         gid = pwd.getpwnam(group).pw_gid
#         os.chown(path, uid, gid)
#     except KeyError:
#         pass


def bash(cmd):
    """
    run a bash shell command
    执行bash命令
    """
    return subprocess.call(cmd, shell=True)


# def mkdir(dir_name, username='', mode=755):
#     """
#     insure the dir exist and mode ok
#     目录存在，如果不存在就建立，并且权限正确
#     """
#     cmd = '[ ! -d %s ] && mkdir -p %s && chmod %s %s' % (dir_name, dir_name, mode, dir_name)
#     bash(cmd)
#     if username:
#         chown(dir_name, username)


# 将对象列表转换为str
def object2str(object_list):
    """
    将对象列表转换为str
    """
    if len(object_list) < 3:
        return ' '.join([obj.name for obj in object_list])
    else:
        return '%s ...' % ' '.join([obj.name for obj in object_list[0:2]])


def captcha2():
    letter_cases = "abcdefghjkmnpqrstuvwxy"
    upper_cases = letter_cases.upper()
    numbers = ''.join(map(str, range(3, 10)))
    init_str = ''.join((letter_cases, upper_cases, numbers))

    # width = 60 * 4
    # height = 60
    width = 100
    height = 32

    image = Image.new('RGB', (width, height), (255, 255, 255))
    font_file = os.path.join(BASE_DIR, 'static/fonts/consola.ttf')

    # 创建Font对象:
    font = ImageFont.truetype(font_file, 36)

    # 创建Draw对象:
    draw = ImageDraw.Draw(image)

    # 绘制干扰线
    line_num = random.randint(1, 10)
    for i in range(line_num):
        # 起始点
        begin = (random.randint(0, width), random.randint(0, height))
        # 结束点
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill=(0, 0, 0))

    # 绘制干扰点:
    for w in range(width):
        for h in range(height):
            # draw.point((w, h), fill=(0, 0, 0))
            rand_color = (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
            draw.point((w, h), fill=rand_color)

    # 绘制验证码字符:
    # for t in range(4):
    #     rand_str = chr(random.randint(65, 90))
    #     rand_color2 = (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
    #     draw.text((60 * t + 10, 10), rand_str, font=font, filter=rand_color2)

    rand_chars = random.sample(init_str, 4)
    strs = ' %s ' % ''.join(rand_chars)  # 每个字符前后以空格隔开
    font_width, font_height = font.getsize(strs)
    rand_color2 = (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
    draw.text(((width - font_width) / 3, (height - font_height) / 3), strs, font=font, fill=rand_color2)

    # 模糊:
    # image = image.filter(ImageFilter.BLUR)
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强（阈值更大）
    # image.save('code.jpg', 'jpeg')
    return image, strs.strip()
