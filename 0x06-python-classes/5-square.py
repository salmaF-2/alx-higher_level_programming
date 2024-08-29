#!/usr/bin/python3
"""
This module contains the Square class
"""


class Square:
    """
    Represents a square
    """

    def __init__(self, size=0):
        """
        Initializes a square instance
        Args:
            size (int): The size of the square (default is 0)
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square
        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square
        Args:
            value (int): The size of the square
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calcul the area of square
        Returns:
            int: The area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with #
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
