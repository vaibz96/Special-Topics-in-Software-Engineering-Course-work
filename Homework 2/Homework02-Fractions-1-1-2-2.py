"""

@homework: HW 02 - Fractions
@author: Vaibhav Vishnu Shanbhag
@date: 02/06/2019
@time: 6:10:37 AM
This assignment demonstrates the python code for fraction function for fraction calculation
"""
import math
class Fraction:
    """ Support addition, subtraction, multiplication, and division of fractions"""
    def __init__(self, numerator, denominator):
        """This will the initialization of attributes for the instances"""

        self.numerator = numerator
        self.denominator = denominator

        if denominator==0:
            raise ZeroDivisionError("Output will be Infinity")
    

    def __str__(self):

        return str(self.numerator)+"/"+str(self.denominator)

    def getNumerator(self):

        return self.numerator

    def getDenominator(self):

        return self.denominator


    def plus(self, other):
        numerator = self.getNumerator() * other.getDenominator() + self.getDenominator()*other.getNumerator()
        denominator = self.getDenominator() * other.getDenominator()
        return Fraction(numerator, denominator)

    def minus(self, other):
        numerator = (self.getNumerator() * other.getDenominator()) - (other.getNumerator() * self.getDenominator())
        denominator = self.getDenominator() * other.getDenominator()
        return Fraction(numerator, denominator)

    def times(self, other):
        numerator = self.getNumerator() * other.getNumerator()
        denominator = self.getDenominator() * other.getDenominator()
        return Fraction(numerator, denominator)

    def divide(self, other):
        numerator = self.getNumerator() * other.getDenominator()
        denominator = self.getDenominator() * other.getNumerator()
        return Fraction(numerator, denominator)
        
    def equal(self, other):
        return self.numerator*other.denominator==other.numerator*self.denominator
            

def tests():
    """The second print statement is what you asked for the update in the tests function"""
    f12 = Fraction(1, 2)
    f44 = Fraction(4, 4)
    print(f"{f12} + {f12}  = {f12.plus(f12)} [4/4]")
    print(f"{f44} - {f12} = {f44.minus(f12)} [4/8]")
    print(f"{f12} + {f12} - {f12} = {f12.plus(f12).minus(f12)} [4/8]")
    f44 = f12.plus(f12)
    f128 = f12.plus(f44)
    f32 = Fraction(3, 2)
    print(f"{f12} + {f44} = {f12.plus(f44)} [12/8]")
    print(f"{f128} == {f32} [True]")

def get_number(prompt):
    """ read and return an integer from the user."""
    while True:
        inp = input(prompt)
        try:
            return int(inp)
        except ValueError:
            print('Error: {inp} is not a number. Please try again...')


def main():
    """ Fraction calculations """
    print('Welcome to the fraction calculator!')
    numerator = get_number("Fraction 1 numerator: ")
    denominator = get_number("Fraction 1 denominator: ")
    operator = input("Operation (+, -, *, /): ")
    numerator_2 = get_number("Fraction 2 numerator: ")
    denominator_2= get_number("Fraction 2 denominator: ")
    result = None
    f1 = Fraction(numerator, denominator)
    f2 = Fraction(numerator_2, denominator_2)
    print(f1,f2)
    
    if operator=="+":
        print(f"{f1} + {f2} == {f1.plus(f2)}")
    elif operator=="-":
        print(f"{f1} - {f2} == {f1.minus(f2)}")
    elif operator=="*":
        print(f"{f1} - {f2} == {f1.times(f2)}")
    else:
        print(f"{f1} - {f2} == {f1.divide(f2)}")
    
    print(f"{f1} + {f2} -{f2}=={f1.plus(f2).minus(f2)}")
    f12p2 = f1.plus(f2).plus(f2)
    f12m2 = f1.plus(f2).minus(f2)
    print(f"{f12p2} = {f12m2} == {f12p2.equal(f12m2)}")
    
# apply f1 operator f2 and print the result
if __name__ == '__main__':
    tests()  # predefined tests
    main()   # interact with the user










