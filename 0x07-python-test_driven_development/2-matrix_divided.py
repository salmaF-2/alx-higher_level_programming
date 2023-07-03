#!/usr/bin/python3
"""
matrix_divided is a function that divides the given matrix
by the parameter "div", and returns the divided matrix
"""


def matrix_divided(matrix, div):
        """ 
        Description:
            Divides all elements of a matrix by "div"
            must be a list of lists of integers or floats
            matrix must be of the same size
            "div" is an int/float or is 0
        Args:
            matrix (list): A list of lists containing integers or floats.
            div (int or float): The number to divide the matrix elements by.
        Returns:
            list: new matrix with elements divided by div rounded 
            to 2 decimal places
        Raises:
            TypeError: not a list of lists of integers/floats or div is not number.
            ZeroDivisionError: If div is equal to 0.
        """

        if type(matrix) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        size = None
        for x in matrix:
            if type(x) is not list:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            if size is None:
                size = len(x)
            elif size != len(x):
                raise TypeError("Each row of the matrix must have the same size")
            for i in x:
                if type(i) is not int and type(i) is not float:
                    raise TypeError("matrix must be a matrix (list of lists) of \
                        integers/floats")

        if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")

        new = []
        for x in matrix:
            new_x = [round(i / div, 2) for i in x]
            new.append(new_x)

        return new
