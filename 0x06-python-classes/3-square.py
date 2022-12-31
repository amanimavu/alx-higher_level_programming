#!/usr/bin/python3
'''
   Create a Square class
   then initialize the field size safely
   checking if it is an integer
   or if it is less than 0

   Then write a method that computes the
   area of the squarei
'''


class Square:
    '''initialize the size attribute using __init__'''
    def __init__(self, size=0):
        self.safe_size = size

    '''use @property to check whether size is int or less than 0'''
    @property
    def safe_size(self):
        return self.__size

    @safe_size.setter
    def safe_size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    '''compute area of the square'''
    def area(self):
        return self.safe_size ** 2
