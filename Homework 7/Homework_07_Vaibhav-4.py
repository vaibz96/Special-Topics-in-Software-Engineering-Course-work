"""
@author: Vaibhav Vishnu Shanbhag
@homework: HW 05
@date: 03/12/2019
@time: 05:08:11 PM
This code is to practice lists, tuples, dictionaries and sets using conatainers in python
"""

import unittest
from collections import defaultdict, Counter, OrderedDict

def anagram(str1, str2):
    """Part 1.1 Anagrams using lists and strings"""
    return sorted(str1.lower()) == sorted(str2.lower())

def anagram_dd(str1, str2):
    dd = defaultdict(int)
    """Part 1.2: Anagrams using defaultdict"""
    for i in str1.lower():
        dd[i] += 1
    for c in str2.lower():
        if c in dd and len(str1) == len(str2):
            dd[c] -= 1
        else:
            return False
    return any([True for value in dd.values() if value == 0])

def counter_anagram(str1, str2):
    """Part 1.3: Anagrams using Counters"""
    return Counter(str1.lower()) == Counter(str2.lower())

def covers_alphbet(sentence):
    a = 'abcdefghijklmnopqrstuvwxyz'
    """ 
        the set operation will take all the unique values and save in set container
        now set minus operation will take out all the common values and if the result is None 
        then it will return True that is why the not logical operation is used
    """
    return (set(sentence.lower()) >= set(a))

def book_index(words):
    dd = defaultdict(set)
    for key, value in iter(words):
        dd[key].add(value)
    return sorted(dd.items())

class Test_Anagram(unittest.TestCase):
    def test_anagram(self):
        self.assertEqual(anagram('cinema', 'iceman'), True)
        self.assertEqual(anagram('dormitory', 'DIRTYROOM'), True)
        self.assertEqual(anagram('123764', '376421'), True)
        self.assertEqual(anagram('def', 'fed'), True)
        self.assertEqual(anagram('cat', 'tac'), True)
        self.assertEqual(anagram('hi-tech', 'i-techh'), True)
        self.assertEqual(anagram(')(*&^%$#@!', '!@#$%^&*()'), True)
        """Here the example gives false value because of different length"""
        self.assertEqual(anagram('dormitory', 'DIRTYROOM12'), False)

class Test_Anagram_dd(unittest.TestCase):
    def test_anagram_dd(self):
        self.assertEqual(anagram_dd('cinema', 'iceman'), True)
        self.assertEqual(anagram_dd('dormitory', 'dirtyroom'), True)
        self.assertEqual(anagram_dd('123764', '376421'), True)
        self.assertEqual(anagram_dd('def', 'fed'), True)
        self.assertEqual(anagram_dd('CAt', 'tac'), True)
        self.assertEqual(anagram_dd('hi-tech', 'i-techh'), True)
        self.assertEqual(anagram_dd(')(*&^%$#@!', '!@#$%^&*()'), True)
        self.assertEqual(anagram_dd("hello world", "hello"), False)

class Test_Anagram_Counter(unittest.TestCase):
    def test_anagram_counter(self):
        self.assertEqual(counter_anagram('cinema', 'iceman'), True)
        self.assertEqual(counter_anagram('dormitory', 'dirtyroom'), True)
        self.assertEqual(counter_anagram('123764', '376421'), True)
        self.assertEqual(counter_anagram('Def', 'Fed'), True)
        self.assertEqual(counter_anagram('cat', 'tac'), True)
        self.assertEqual(counter_anagram('hi-tech', 'i-techh'), True)
        self.assertEqual(counter_anagram(')(*&^%$#@!', '!@#$%^&*()'), True)

class Test_Covers_Alphabet(unittest.TestCase):
    def test_covers_alphabet(self):
        self.assertEqual(covers_alphbet("AbCdefghiJklomnopqrStuvwxyz"), True)
        self.assertEqual(covers_alphbet("We promptly judged antique ivory buckles for the next prize"), True)
        self.assertEqual(covers_alphbet("xyz"), False)
        self.assertEqual(covers_alphbet('abcdefghijklmnopqrstuvwxyz'), True)
        self.assertEqual(covers_alphbet('aabbcdefghijklmnopqrstuvwxyzzabc'), True)
        self.assertEqual(covers_alphbet('The quick brown fox jumps over the lazy dog'), True)
        self.assertEqual(covers_alphbet('The quick, brown, fox; jumps over the lazy dog!'), True)

class Test_Book_Index(unittest.TestCase):
    def test_book_index(self):
        woodchucks = [('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1),('woodchuck', 1), ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2),('could', 2), ('chuck', 1), ('wood', 1)]
        woodchucks_1 = [('a', 'one'), ('a', 'two'), ('a', 'three'), ('woodchuck', 'one'), ('woodchuck', 'two'), ('woodchuck', 'three')]
        self.assertEqual(book_index(woodchucks_1), [('a', {'one', 'three', 'two'}), ('woodchuck', {'one', 'three', 'two'})])
        self.assertEqual(book_index(woodchucks), [('a', {1}), ('chuck', {1, 3}), ('could', {2}), ('how', {3}), ('if', {1}), ('much', {3}), ('wood', {1, 3}), ('woodchuck', {1, 2}), ('would', {2})])

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)



