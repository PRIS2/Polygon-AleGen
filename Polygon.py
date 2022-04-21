from PolygonType import PolygonType
from Utils import count_vertices_distance


class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices
        self.perimeter = self.__count_perimeter()
        self.type = self.__get_polygon_type()

    def __count_perimeter(self):
        current_perimeter = 0
        vertices_number = len(self.vertices)
        if vertices_number >= 3:
            for i in range(vertices_number - 1):
                vertex_1 = self.vertices[i]
                vertex_2 = self.vertices[i + 1]
                current_perimeter += count_vertices_distance(vertex_1, vertex_2)
        return current_perimeter

    def __get_polygon_type(self):
        return PolygonType.convex

