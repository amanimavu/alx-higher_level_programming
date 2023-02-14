#!/usr/bin/python3

"""
module: rectangle
resources: class Rectangle that inherits from Base class
"""
from base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The __init__ method is a magic method
        that initializes instance variables every
        time an object is created.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        The width getter method returns the size
        of the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        The corresponding setter method is used to
        set the size of the rectangle.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        The height getter method is used to return the size
        of the rectangle's height to the user.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        While the corresponding height setter method is used
        to the the size of the rectangle's height.
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 1:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        The x getter method is used to set the x coordinate
        position of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Its corresponding setter method is used to set x
        coordinate of the rectangle
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        The y getter method return the y coordinate
        position of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        The corresponding setter method is used to
        set the y coordinate position.
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        The area method is used to return the area of the
        specified instance rectangle to the user
        """
        return self.width * self.height

    def display(self):
        """
        The display method print a graphical representation
        of the rectangle using #
        """
        for row in self.height:
            print(self.width * '#')

    def __str__(self):
        """
        The magical __str__ method is used to return the details
        of the rectangle in a manner that is well presented
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.x, self.y, self.width, self.height)
                )
