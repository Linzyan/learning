import sys
sys.path.append('D:\python\git learning\learning')
import Josephus
import reader
def test_output():
    test_list = ['1', '2', '3']
    test_start = 0
    test_step = 3
    test_jose = Josephus.Josephus(int(test_start), int(test_step), test_list)
    for i in range(len(test_list)-1):
        test_jose.next()
    assert test_jose.people[0] == '2'
def test_txt_reader():
    test = reader.Txt_reader("test.txt")
    test.read_file()
    assert(len(test.content) == 3)
def test_csv_reader():
    test = reader.Csv_reader("test.csv")
    test.read_file()
    assert(len(test.content) == 3)
def test_zip_reader():
    test = reader.Zip_reader("test.zip")
    test.read_file()
    assert(len(test.content) == 3)