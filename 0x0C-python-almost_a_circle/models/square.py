#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ square class inherits from Rectangle """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size func """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter func """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update the class Square by adding the public method """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        if len(args) == 0 and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

        def to_dictionary(self):
            """ dictionary representation """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """ square str """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
