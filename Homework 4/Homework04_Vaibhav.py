"""
@author: Vaibhav Vishnu Shanbhag
@homework: HW 03
@date: 12/02/2019
@time: 08:09:57
This code Implements iterating over lists, ranges, and strings using
for and while loops as well as using a generator of random integers.
"""

"""Part 1"""
import unittest

def count_vowels(s):
    n = 0
    for i in s:
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            n +=1
    return n

class CountVowelsTest(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('hEllO wrld'.lower()), 2)
        self.assertEqual(count_vowels('hll wrld'), 0)
        self.assertEqual(count_vowels(' '), 0)
        self.assertEqual(count_vowels('23_)(!&&@(U'), 1)
        self.assertEqual(count_vowels('Ebvdysh1hhs9jhbUO'), 3)


"""Part 2"""

def arg(target, list):
    p = None
    for offset, c in enumerate(list):
         if target == c:
            p = offset
    return p

class ArgTest(unittest.TestCase):
    def test_arg(self):
        self.assertEqual(arg(42, [42, 33, 21, 33]), 0)
        self.assertEqual(arg(33, [42, 33, 21, 33]), 3)
        self.assertEqual(arg('p', 'apple'), 2)
        self.assertEqual(arg('s', 'apple'), None)



"""Part 3"""
""" I have extended the code for HW03 and i have attached the file"""

"""Part 4"""
def my_enumerate(seq):
    count = 0
    while count<len(seq):
        for i in seq:
            yield count, i
            count+=1

class EnumerateTest(unittest.TestCase):
    def test_my_enumerate(self):
        self.assertTrue(list(my_enumerate("hi")) == list(enumerate("hi")))
        self.assertTrue(list(my_enumerate("oiuygbd")) != list(enumerate("eurghfdjs")))
        self.assertTrue(list(my_enumerate("oiuygbd")) != list(enumerate("eurghfdjs")))


if __name__ == '__main__':
# note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)
