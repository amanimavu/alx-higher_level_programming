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
        self.size = size

    '''use @property to check whether size is int or less than 0'''
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    '''compute area of the square'''
    def area(self):
        return self.size ** 2

    '''print the square using #'''
    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print("")
