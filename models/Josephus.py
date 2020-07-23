class Josephus(object):
    def  __init__(self, start, step, people):
        self.people = people
        self.start = start
        self.step = step
        self.total_number = len(self.people)
    def append(self, person):
        self.people.append(person)
    def pop(self, person):
        self.people.pop(person)
    def __iter__(self):
        return self
    def next(self):
        if len(self.people) > 0:
            out_key = (self.start + self.step - 1) % self.total_number
            self.pop(out_key)
            self.start = out_key
            self.total_number -= 1
        else:
            raise StopIteration