#!/usr/bin/python3
<<<<<<< HEAD
'''Module for Rectangle class.'''
=======
"""Model for Base"""
>>>>>>> bc9a2935519e5669f53176a25eba978cc55e4c59
from models.base import Base


class Rectangle(Base):
<<<<<<< HEAD
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''
=======
    """Class for Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init for Base"""
>>>>>>> bc9a2935519e5669f53176a25eba978cc55e4c59
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
<<<<<<< HEAD
        '''Width of this rectangle.'''
=======
        """Getter for width"""
>>>>>>> bc9a2935519e5669f53176a25eba978cc55e4c59
        return self.__width

    @width.setter
    def width(self, value):
<<<<<<< HEAD
        self.validate_integer("width", value, False)
=======
        """Setter for width"""
        self.int_validation("width", value)
>>>>>>> bc9a2935519e5669f53176a25eba978cc55e4c59
        self.__width = value

    @property
    def height(self):
<<<<<<< HEAD
        '''Height of this rectangle.'''
=======
        """Getter for height"""
>>>>>>> bc9a2935519e5669f53176a25eba978cc55e4c59
        return self.__height

    @height.setter
    def height(self, value):
<<<<<<< HEAD
        self.validate_integer("height", value, False)
=======
        """Setter for height"""
        self.int_validation("height", value)
>>>>>>> bc9a2935519e5669f53176a25eba978cc55e4c59
        self.__height = value

    @property
    def x(self):
<<<<<<< HEAD
        '''x of this rectangle.'''
=======
        """Getter for x"""
>>>>>>> bc9a2935519e5669f53176a25eba978cc55e4c59
        return self.__x

    @x.setter
    def x(self, value):
<<<<<<< HEAD
        self.validate_integer("x", value)
=======
        """Setter for x"""
        self.int_validation("x", value)
>>>>>>> bc9a2935519e5669f53176a25eba978cc55e4c59
        self.__x = value

    @property
    def y(self):
<<<<<<< HEAD
        '''y of this rectangle.'''
=======
        """Getter for y"""
>>>>>>> bc9a2935519e5669f53176a25eba978cc55e4c59
        return self.__y

    @y.setter
    def y(self, value):
<<<<<<< HEAD
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''Method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''Computes area of this rectangle.'''
        return self.width * self.height

    def display(self):
        '''Prints string representation of this rectangle.'''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        '''Returns string info about this rectangle.'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal method that updates instance attributes via */**args.'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
=======
        """Setter for y"""
        self.int_validation("y", value)
        self.__y = value

    def int_validation(self, name, value):
        """Validates input"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if (name == "height" or name == "width") and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))
        if (name == "y" or name == "x") and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    def area(self):
        """Area getter"""
        return self.__height * self.__width

    def display(self):
        """Displays the shape"""
        rect = "" + ' ' * self.__x
        rect += str('#') * self.__width
        rect = '\n' * self.__y + '\n'.join(
                    list(rect for index in range(self.__height)))
        print(rect)

    def __str__(self):
        """returns information about the shape"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        """updates the rectangle??? i think"""
        index = 0
        if args is not None and len(args) != 0:
            for argument in args:
                index += 1
                if index == 1:
                    self.id = argument
                elif index == 2:
                    self.__width = argument
                elif index == 3:
                    self.__height = argument
                elif index == 4:
                    self.__x = argument
                elif index == 5:
                    self.__y = argument
        else:
            for key, values in kwargs.items():
                setattr(self, key, values)

    def to_dictionary(self):
        """makes a self dictionary"""
        dictionary = {}
        for index in ["id", "width", "height", "x", "y"]:
            dictionary[index] = getattr(self, index)
        return dictionary
>>>>>>> bc9a2935519e5669f53176a25eba978cc55e4c59
