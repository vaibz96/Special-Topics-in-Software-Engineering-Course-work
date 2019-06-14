"""
@author: Vaibhav Vishnu Shanbhag
@homework: HW 05
@date: 02/24/2019
@time: 05:08:11 PM
This code Implements a class for string methods and the automated testing
"""
import unittest

"""Part 1"""
def reverse(str):
    string = ''
    index_val = len(str)
    """
    While loop will start with the length of the string and decrement the index
    and return the value at that index
    """
    while index_val:
        index_val -= 1
        string += str[index_val]
    return string

"""Part 2"""
def rev_enumerate(str):
    string=''
    index_val = len(str)
    """
    While loop will start with the length of the string and decrement the index
    and return the value at that index
    """
    while index_val:
        index_val -= 1
        string += str[index_val]
    count = len(string)
    """
    the count will store the length of the string
    and the while iterate through each string returning the count in reverse order as an offset in reverse order
    """
    while count:
        for i in string:
            """the default index of any element in a string is 0 I have yielded count-1 """
            yield count-1, i
            count -= 1

"""Part 3"""
def find_second(s1, s2):
    """
    here this function returns the substring s1 in s2 string s2.find(s1) will return the index of the string s1
    and s2.find(s1)+1 will give index from its second occurrence note:index==offset
    at second index
    """
    return s2.find(s1, s2.find(s1)+1)

"""Part 4"""
def get_lines():
    """
    the f variable will open the text file using
    open function and f.close() will close the same text file
    """
    f = open('test.txt', 'r')
    new_line = ''
    for line in f:
        line = line.rstrip("\r\n")
        if line.endswith('\\'):
            new_line += line.rstrip('\\')
            continue
        new_line += line
        find_hash = new_line.find('#')
        if find_hash == 0:
            new_line = ''
        if find_hash >= 1:
            new_line = new_line[:find_hash]
            yield new_line
            new_line = ''
        if find_hash == -1:
            yield new_line
            new_line = ''
    f.close()
class Reverse_Test(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse('hi my bro'), 'orb ym ih')
        self.assertFalse(reverse('hi my name') == 'ieurfygvcj')
        self.assertEqual(reverse('8976'), '6798')
        self.assertFalse(reverse('my name')== 'myname')

class Reverse_Enumerate_Test(unittest.TestCase):
    def test_rev_enumerate(self):
        self.assertEqual(list(rev_enumerate("hi bro!")),[(6, '!'), (5, 'o'), (4, 'r'), (3, 'b'),\
                                                         (2, ' '), (1, 'i'), (0, 'h')])

class Test_Second_Occurance(unittest.TestCase):
    def test_find_second(self):
        self.assertEqual(find_second('iss', 'Mississippi'), 4)
        self.assertEqual(find_second('abba', 'abbabba'), 3)
        self.assertEqual(find_second('x', 'abbabba'), -1)

class GetLinesTest(unittest.TestCase):
    def test_get_lines(self):
        expect = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>', '<line4.1 line4.2>', '<line5>', '<line6>']
        result = list(get_lines())
        self.assertEqual(result, expect)

if __name__=='__main__':
    unittest.main(exit=False, verbosity=2)


