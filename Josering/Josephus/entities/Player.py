class Counter(object):
    count = 0
class Player(Counter):
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender 
        self.age = age
        Counter.count += 1
        if self.age < 0:
            self.age = 0
        if gender not in ['男', '女']:
            self.gender = ValueError