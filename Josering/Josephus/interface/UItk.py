import sys
sys.path.append('F:\python\learn\learning\Josering') 
from Josephus.interface import output
from tkinter import *
class Ui_window():
    def __init__(self):
        self.on_hit = False #控制是否显示
        self.window = Tk() #初始化Tk
        self.window.title("josephus-ring") #窗口的标题
        self.window.geometry("550x550") #窗口大小
        self.var = StringVar() #设置字符串变量
        self.var2 = StringVar()
        self.var3 = StringVar() 
    def creat_control(self):
        self.l1 = Label(self.window, text = '选择读取文件',bd = 10, font = ("Arial", 12), width = 15, height = 2)
        self.l1.grid(row = 4, column = 1) #安置
        l2 = Label(self.window, text = '开始位置', bd = 10, font = ("Arial", 11), width = 5, height = 2)
        l2.grid(row = 1, column = 8)
        l3 = Label(self.window, text = '步进量', bd = 10, font = ("Arial", 11), width = 5, height = 2)
        l3.grid(row = 2, column = 8)
        l4 = Label(self.window, textvariable = self.var3, bd = 10, font = ("Arial", 11), width = 30, height = 2)
        l4.grid(row = 4, column = 8)
        self.e1 = Entry(self.window, show = None) #输入文本框
        self.e1.place(x = 350, y=20, width = 50, height = 25)
        self.e2 = Entry(self.window, show = None) #输入文本框
        self.e2.place(x = 350, y=70, width = 50, height = 25)
        r1 = Radiobutton(self.window, text = "from txt", variable = self.var, value = "F:\python\learn\learning\Josering\data\player_list.txt", command = self.print_selection)#设置选项（三种文件）
        r1.grid(row = 1, column = 1)
        r2 = Radiobutton(self.window, text = "from csv", variable = self.var, value = "F:\python\learn\learning\Josering\data\player.csv", command = self.print_selection)
        r2.grid(row = 2, column = 1)
        r3 = Radiobutton(self.window, text = "from zip", variable = self.var, value = "F:\python\learn\learning\Josering\data\player.zip", command = self.zip_selection)
        r3.grid(row = 3, column = 1)
        self.lb = Listbox(self.window, listvariable = self.var2)
        self.lb.grid(row = 5, column = 1)
        b1 = Button(self.window,text = 'pick this', width=15, height = 3, command = self.pick_file)
        b1.grid(row = 6, column = 1)
        b2 = Button(self.window,text = '约瑟夫游戏开始', width=15, height = 3, command = self.out_put)
        b2.grid(row = 3, column = 8)
    def print_selection(self):
        global inter
        self.lb.delete(0,END)
        file_name = self.var.get()
        inter = output.Interface()
        inter.creat_reader(file_name)
        self.l1.config(text = "人员列表" )
        for x in inter.reader.content:
            self.lb.insert('end', x)        
    def zip_selection(self):
        global inter
        self.lb.delete(0,END)
        file_name = self.var.get()
        inter = output.Interface()
        inter.creat_reader(file_name)
        for x in inter.reader.each_files:
            self.lb.insert('end', x)
        self.l1.config(text = "选择文件列表" )
        self.on_hit = True     
    def pick_file(self):
        global inter
        if self.on_hit == True:
            index = self.lb.curselection()
            inter.reader.read_zip(index[0])
            self.lb.delete(0,END)
            self.l1.config(text = "人员列表" )
            for x in inter.reader.content:
                self.lb.insert('end', x)
            self.on_hit = False
        else:
            return False
    def out_put(self):
        start = int(self.e1.get())
        step = int(self.e2.get())
        inter.set_start(start)
        inter.set_step(step)
        person = inter.creat_person_list()
        inter.creat_josephus_ring(person)
        self.var3.set(inter.output())   
    def ui_show():
        ui = Ui_window()
        ui.creat_control()
        ui.window.mainloop()
    ui_show()