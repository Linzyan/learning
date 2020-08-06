#接口定义
import sys
sys.path.append('F:\python\learn\learning\Josering')
from pathlib import Path 
import os
from Josephus.adapter import readers as rd 
from Josephus.entities import Player as py
from Josephus.domain.use_case import josephus
class Interface():
    def __init__(self):
        self.reader = None
        self.start = -1
        self.step = -1
    def creat_reader(self, file_name): #选择reader
        path = os.path.splitext(file_name)[1]
        if path == ".txt":
            self.reader = rd.Txt_reader(file_name)
        elif path == ".csv":
            self.reader = rd.Csv_reader(file_name)
        elif path == ".zip":
            self.reader = rd.Zip_reader(file_name)
        else:
            raise FileNotFoundError
        self.reader.read_file()
    def creat_person_list(self): #创建人员列表
        people = []
        for i in range(len(self.reader.content)):
            people.append(py.Player(self.reader.content[i][0], self.reader.content[i][1], int(self.reader.content[i][2])))
        return people
    def set_start(self, start): #设置起始位置
        self.start=int(start)
        if self.start < 0:
            raise ValueError
    def set_step(self, step): #设置步进量
        self.step = step
        if self.step < 1:
            raise ValueError
    def creat_josephus_ring(self, person): #创建约瑟夫实例
        if self.start  < len(person)-1:
            self.jose = josephus.Josephus(self.start, self.step, person)
        else:
            raise  ValueError
    def output(self): #输出存活
        for i in range(self.jose.total_number-1):
            self.jose.next()
        return("存活的人是%s, 性别为%s, 年龄是%s"%(self.jose.people[0].name, self.jose.people[0].gender, self.jose.people[0].age))