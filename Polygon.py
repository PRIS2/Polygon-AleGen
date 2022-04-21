from PolygonType import PolygonType


class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices
        self.perimeter = self.__count_perimeter()
        self.type = self.__get_polygon_type()

    def __count_perimeter(self):
        return 0

    def __get_polygon_type(self):
        return PolygonType.convex

