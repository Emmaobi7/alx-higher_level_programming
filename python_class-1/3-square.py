#!/usr/bin/python3
class Square:
    def __init__(self, size=0):

        if type(size) != int:
            raise TypeError("must be integer")
        elif size < 0:
            raise ValueError("not less than 0")
        

        self.__size = size

    def area(self):
        return self.__size * self.__size

