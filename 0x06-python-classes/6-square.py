#!/usr/bin/python3
'''
   Create a Square class
   then initialize the field size safely
   checking if it is an integer
   or if it is less than 0

   Then write a method that computes the
   area of the square

   Write a method that prints the squar using #

'''


class Square:
    '''initialize the size attribute using __init__'''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if len(position) == 2 and (
            (type(position[0]) is int and position[0] >= 0) and
            (type(position[1]) is int and position[1] >= 0)
        ):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    '''compute area of the square'''
    def area(self):
        return self.size ** 2

    '''print the square using # considering the position attribute'''
    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for j in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                for j in range(self.size):
                    print("#", end="")
                print("")
