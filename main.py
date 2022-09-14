#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
  @FileName  :main.py
  @Time      :2022/9/13 20:57
  @Software  :PyCharm
  @Author    :Administrator
-------------------------------------------------
"""
import os
import rename
from rename import*


def main():
    os.system('python rename.py')
    for drawable in get_appName():
        if os.path.exists(drawable + '.png'):
            os.remove(drawable + '.png')
        else:
            pass
        if os.path.exists('icons/' + drawable + '.png'):
            os.remove('icons/' + drawable + '.png')
        else:
            pass


if __name__ == "__main__":
    icons_dir = "icons"
    text = 'backup.xml'
    #print("当前工作文件夹为 %s,所有文件都应处于该文件夹内。" % os.getcwd())
    if os.path.exists(icons_dir) and os.path.exists(text):
        main()
    else:
        print("icons文件夹不存在，backup.xml文件不存在，请检查！")
