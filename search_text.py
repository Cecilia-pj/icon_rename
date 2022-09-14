#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
  @FileName  :search_text.py
  @Time      :2022/9/13 19:57
  @Software  :PyCharm
  @Author    :Administrator
-------------------------------------------------
"""
import os

text = 'backup.xml'
package_dict = {}


def get_appName():
    i = 1
    with open(text, 'r', encoding='utf-8') as file_obj:
        data = file_obj.read()
        #print(data)
        info = data.split("<icon name=")
        while i < len(info):
            #print(data.split("<icon name=")[i].split(' />')[0].split('"')[1])
            # print(info[i].split(' />')[1:][:-1])
            j = 0
            package_list = []
            drawable = info[i].split(' />')[0].split('"')[-2]
            while j <= len(info[i].split(' />')[1:][:-1])-1:
                if len(info[i].split(' />')[1:][:-1][j].split('packageName=')) >1:
                    # print(info[i].split(' />')[1:][:-1][j].split('packageName=')[1].split('"')[1])
                    package_name = info[i].split(' />')[1:][:-1][j].split('packageName=')[1].split('"')[1]
                    package_list.append(package_name)
                    final_list = list(set(package_list))
                j += 1
            i += 1
            package_dict[drawable] = final_list
        return package_dict


if __name__ == "__main__":
    print("当前工作文件夹为 %s,所有文件都应处于该文件夹内。" % os.getcwd())
    if os.path.exists(text):
        get_appName()

    else:
        print('backup.xml文件不存在，请检查！')

