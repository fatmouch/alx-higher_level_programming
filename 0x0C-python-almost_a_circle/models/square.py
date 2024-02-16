#!/usr/bin/python3
<<<<<<< HEAD
"""Define Square class implement Rectangle
"""

=======
"""Square model"""
>>>>>>> bc9a2935519e5669f53176a25eba978cc55e4c59
from models.rectangle import Rectangle


class Square(Rectangle):
<<<<<<< HEAD
    """Square class body
"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization class props in constructor
        """
=======
    """class for square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the square"""
>>>>>>> bc9a2935519e5669f53176a25eba978cc55e4c59
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
<<<<<<< HEAD
        """ return width size
        """
=======
        """size getter"""
>>>>>>> bc9a2935519e5669f53176a25eba978cc55e4c59
        return self.width

    @size.setter
    def size(self, value):
<<<<<<< HEAD
        """module Square height and width
        """
=======
        """size setter"""
>>>>>>> bc9a2935519e5669f53176a25eba978cc55e4c59
        self.width = value
        self.height = value

    def __str__(self):
<<<<<<< HEAD
        """Square class string
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """update square props
        """
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ return dict of class props
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
=======
        """returns information about the shape"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.height)

    def update(self, *args, **kwargs):
        """updates the square??? i think"""
        index = 0
        if args is not None and len(args) != 0:
            for argument in args:
                index += 1
                if index == 1:
                    self.id = argument
                elif index == 2:
                    self.size = argument
                elif index == 3:
                    self.x = argument
                elif index == 4:
                    self.y = argument
        else:
            for key, values in kwargs.items():
                setattr(self, key, values)

    def to_dictionary(self):
        """makes a self dictionary"""
        dictionary = {}
        for index in ["id", "size", "x", "y"]:
            dictionary[index] = getattr(self, index)
        return dictionary
>>>>>>> bc9a2935519e5669f53176a25eba978cc55e4c59
