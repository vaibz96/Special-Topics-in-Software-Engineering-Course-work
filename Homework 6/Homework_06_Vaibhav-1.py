"""
@author: Vaibhav Vishnu Shanbhag
@homework: HW 05
@date: 03/03/2019
@time: 05:00:11 PM
This code Implements functions that perform string operations,
insertion sort and binary search tree and automated test cases to run them
"""

import unittest

"""Part 1"""
def remove_vowels(string):
     item = string.split()
     return "".join([item for item in string if item not in 'aeiouAEIOU'])

"""Part 2"""

def check_pwd(pwd):
    """Any is the python in built function that returns true or false for a given condition """
    return any([True for i in pwd if i.islower()] and [True for i in pwd if i.isupper()] \
               and [True for i in pwd if i[-1].isdigit()])

"""Part 3"""

def insertion_sort(inp):
    r = []
    """Split in order to get a list output"""
    lst = [int(x) for x in inp.split()]

    for offset, i in enumerate(lst):
        """
        Every time this will assign index value zero for new inserted value for comparison
        """
        index = 0
        """
        This loop will check if the index value is less than the length of r and then check at what index the new 
        value can fit after comparing it with the value in input list that is lst
        Here the main idea is using the index value in order to sort the value 
        I have used a new empty list instead of rewriting it into the same list 
        """
        while index < len(r) and r[index] < i:
            index += 1
        r.insert(index, i)
    return r

"""Part 4"""

class BTree:
    def __init__(self, value):
        self.value = value
        self.right_Child = None
        self.left_Child = None

    def find(self, value):
        if value and self.value is not None:
            #print("Comparing:", self.value, value)
            if self.value == value:
                return True
            elif self.value > value:
                return self.left_Child.find(value)
            else:
                return self.right_Child.find(value)
        else:
            return False

    def insert(self, value):
        """
        This function will check for none value and will basically insert the value to the tree when ever user inserts
        the new value
        """
        if value is not None:
            """It will again check if the root value or the existing value is none and perform the further condition"""
            if self.value is None:
                """
                If root value is none it will assign the first insert value as the root value else it will check for 
                the value greater or less than to insert them in the left child or right child position
                """
                self.value = value
            elif self.value > value:
                if self.left_Child is None:
                    """
                    This condition will check if the node has none value if it does it will insert the value to its 
                    left child if its less than the new-value or the root value
                    """
                    self.left_Child = BTree(value)
                else:
                    """
                    If the left child is not none it will again go in loop to check if it is 
                    less than the existing value and insert it accordingly
                    """
                    self.left_Child.insert(value)
            else:
                if self.right_Child is None:
                    """
                    This condition will check if the node has none value it will insert the value to it if 
                    its less than the root value
                    """
                    self.right_Child = BTree(value)
                else:
                    """
                     If the right child is not none it will again go in loop to check if it is
                     greater than the existing value and insert it accordingly
                    """
                    self.right_Child.insert(value)

    def traverse(self):
        tree = []
        if self.left_Child is not None:
            tree += self.left_Child.traverse()
        """
         I have done as said in the hint section created an empty list then extending the list and then
         appending it
        """
        tree.append(self.value)
        if self.right_Child is not None:
            """
             This will be the last part to traverse as mentioned in the hint we will
             not append anything to this
            """
            tree += self.right_Child.traverse()
        return tree


class BinaryTree(unittest.TestCase):
    def test_Btree(self):
        bt = BTree(27)
        bt.insert(1)
        bt.insert(15)
        bt.insert(5)

        new_bt = BTree(65)
        new_bt.insert(6)
        new_bt.insert(7)
        new_bt.insert(8)
        new_bt.insert(160)

        self.assertEqual(bt.find(27), True)
        self.assertEqual(bt.find(15), True)
        self.assertEqual(new_bt.find(8), True)
        self.assertEqual(bt.traverse() == [1, 5, 15, 27], True)
        self.assertEqual(new_bt.traverse() == [6, 7, 8, 65, 160], True)

class RemoveVowelsTest(unittest.TestCase):
    def test_remove_vowels(self):
        self.assertEqual(remove_vowels('hello world'), 'hll wrld')
        self.assertEqual(remove_vowels('bad weather'), 'bd wthr')
        self.assertEqual(remove_vowels('phd'), 'phd')
        self.assertEqual(remove_vowels('aeiou'), '')
        self.assertEqual(remove_vowels('AeIoU'), '')
        self.assertEqual(remove_vowels('e345672uwhsgfdzrt4q4567w'), '345672whsgfdzrt4q4567w')

class PasswordTest(unittest.TestCase):
    def test_password(self):
        self.assertEqual(check_pwd('hello world'), False)
        self.assertEqual(check_pwd('hello world4A'), True)
        self.assertEqual(check_pwd('svywisjn!sgwbsuwA'), False)
        self.assertEqual(check_pwd('gdhyAgbhgghdiuA1'), True)

class SortTest(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort('1 5 3 3'), [1, 3, 3, 5])
        self.assertEqual(insertion_sort('1 0 3 7 3 5 4 2 7 8 4 9'), [0, 1, 2, 3, 3, 4, 4, 5, 7, 7, 8, 9])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)


