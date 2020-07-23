# 实现三种类分装，统一接口
#-*- coding: utf-8 -*-
import os
import csv
import zipfile
from pathlib import Path
class Reader(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.path = os.path.splitext(file_name)[1]
        for x in Reader.__subclasses__():
            if self.path == x.path:
                self.func = x(file_name)
    def read_file(self):
        return self.func.read_file()
class Txt_reader(Reader):
    path = ".txt"
    def __init__(self, file_name):
        self.file_name = file_name
        self.content = []
    def read_file(self):
        f = open(self.file_name, 'r', encoding='utf-8')
        for line in f.readlines():
            eachline = line.strip("\n")
            self.content.append(eachline.split())
        f.close()
        print(self.content)
class Csv_reader(Reader):
    path = ".csv"
    def __init__(self, file_name):
        self.file_name = file_name
        self.content = []
    def read_file(self):
        with open(self.file_name, "r", encoding = "utf-8-sig") as f:
            reader = csv.reader(f)
            for row in reader:
                eachrow = row[0].strip("/t")
                self.content.append(eachrow.split())
        print(self.content)
class Zip_reader(Reader):
    path = ".zip"
    def __init__(self, file_name):
        self.file_name = file_name
        self.content = []
    def read_file(self):
        file_list = zipfile.ZipFile(self.file_name, "r")
        for each_file in file_list.namelist():
            print("file:", each_file)
        index = input("需要阅读第几个文件？（请用阿拉伯数字输入）")
        read_name = file_list.namelist()[int(index) - 1]
        content = file_list.open(read_name, 'r')
        for line in content.readlines():
            line = line.decode("utf-8-sig")
            self.content.append(line.split())
        print(self.content)