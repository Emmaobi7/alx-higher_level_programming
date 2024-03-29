#!/usr/bin/python3  
class Square:

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size


    @size.setter
    def size(self, value):
        
        if type(value) != int:
            raise TypeError("must be integer")
        elif value < 0:
            raise ValueError("not less than 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
