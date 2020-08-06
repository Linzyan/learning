class Josephus(object):
    def  __init__(self, start, step, people):
        self.people = people
        self.start = start
        self.step = step
        self.total_number = len(self.people)
    def add(self, person):
        self.people.append(person)
    def pop(self, id):
        self.people.pop(id)
    def __iter__(self):
        return self
    def next(self):
        if len(self.people) > 0:
            out_key = (self.start + self.step - 1) % len(self.people)
            self.people.pop(out_key)
            self.start = out_key
        else:
            raise StopIteration