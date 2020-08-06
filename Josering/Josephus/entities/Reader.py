class Reader(object):
    def __init__(self, file_name):
        self.file_name = file_name
    def read_file(self):
        return NotImplementedError