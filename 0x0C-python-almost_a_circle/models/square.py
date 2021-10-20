#!/usr/bin/python3
"""
Class square
 """


from models.rectangle import Rectangle
"""
Import class rectangle
"""


class Square(Rectangle):
    """ Init constructor or magic method """

    def __init__(self, size, x=0, y=0, id=None):
        """ Call attributes  """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Method should return [Square] (<id>) <x>/<y> - <size>"""
        id_r = f"({self.id}) "
        x_y_r = f"{self.x}/{self.y} - "
        wid_hei = f"{self.width}"

        return ("[Square] " + id_r + x_y_r + wid_hei)
