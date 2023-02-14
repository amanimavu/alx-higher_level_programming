#!/usr/bin/python3
from .base import Base

"""
module: rectangle
resources: class Rectangle that inherits from Base class
"""


class Rectangle(Base):
    """
    The __init__ method is a magic method
    that initializes instance variables every
    time an object is created.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    """
    The width getter method returns the size
    of the width of the rectangle.
    """
    @property
    def width(self):
        return self.__width

    """
    The corresponding setter method is used to
    set the size of the rectangle.
    """
    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")
        self.__width = width

    """
    The height getter method is used to return the size
    of the rectangle's height to the user.
    """
    @property
    def height(self):
        return self.__height

    """
    While the corresponding height setter method is used
    to the the size of the rectangle's height.
    """
    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 1:
            raise ValueError("height must be > 0")
        self.__height = height

    """
    The x getter method is used to set the x coordinate
    position of the rectangle.
    """
    @property
    def x(self):
        return self.__x

    """
    Its corresponding setter method is used to set x
    coordinate of the rectangle
    """
    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    """
    The y getter method return the y coordinate
    position of the rectangle.
    """
    @property
    def y(self):
        return self.__y

    """
    The corresponding setter method is used to
    set the y coordinate position.
    """
    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    """
    The area method is used to return the area of the
    specified instance rectangle to the user
    """
    def area(self):
        return self.width * self.height

    """
    The display method print a graphical representation
    of the rectangle using #
    """
    def display(self):
        for row in self.height:
            print(self.width * '#')

    """
    The magical __str__ method is used to return the details
    of the rectangle in a manner that is well presented
    """
    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.x, self.y, self.width, self.height)
                )
