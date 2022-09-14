#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
  @FileName  :rename.py
  @Time      :2022/9/13 20:59
  @Software  :PyCharm
  @Author    :Administrator
-------------------------------------------------
"""
import os
import shutil
from search_text import *


def rename_icon():
    for drawable, packag_name in get_appName().items():
        # print(drawable)
        # print(packag_name)
        # print(len(packag_name))
        # 多个包名
        if len(packag_name) > 1:
            # os.rename(drawable, packag_name)
            i = 1
            while i <= len(packag_name):
                # 原文件存在
                if os.path.exists('icons/' + drawable + '.png'):
                    shutil.copy('icons/' + drawable + '.png', '.')
                    # 重命名的文件存在
                    if os.path.exists('icons/' + packag_name[i - 1] + '.png'):
                        os.remove('icons/' + drawable + '.png')
                    else:
                        os.renames(drawable + '.png', 'icons/' + packag_name[i - 1] + '.png')
                else:
                    pass
                i += 1
        # 单个包名
        else:
            if os.path.exists('icons/' + drawable + '.png'):
                if os.path.exists('icons/' + packag_name[0] + '.png'):
                    pass
                else:
                    os.renames('icons/' + drawable + '.png', 'icons/' + packag_name[0] + '.png')
            else:
                pass


if __name__ == "__main__":
    icons_dir = "icons"
    print("当前工作文件夹为 %s,所有文件都应处于该文件夹内。" % os.getcwd())
    if os.path.exists(icons_dir):
        rename_icon()
    else:
        print("icons文件夹不存在。")
