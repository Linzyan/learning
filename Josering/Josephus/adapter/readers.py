# 实现三种类分装，统一接口
import csv
import zipfile
from Josephus.entities import Reader as rd
class Txt_reader(rd.Reader):
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
class Csv_reader(rd.Reader):
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
class Zip_reader(rd.Reader):
    def __init__(self, file_name):
        self.file_name = file_name
        self.content = []
        self.each_files = []
    def read_file(self):
        self.file_list = zipfile.ZipFile(self.file_name, "r")
        for each_file in self.file_list.namelist():
            self.each_files.append(each_file)
        print(self.each_files)
    def read_zip(self, index):
        read_name = self.file_list.namelist()[int(index)]
        content = self.file_list.open(read_name, 'r')
        for line in content.readlines():
            line = line.decode("utf-8-sig")
            self.content.append(line.split())
        print(self.content)
