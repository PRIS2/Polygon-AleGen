from PolygonType import PolygonType
from Utils import count_vertices_distance, cross_product


class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices
        self.perimeter = self.__count_perimeter()
        self.type = self.__get_polygon_type()

    def __count_perimeter(self):
        current_perimeter = 0
        vertices_number = len(self.vertices)
        if vertices_number >= 3:
            for i in range(vertices_number):
                vertex_1 = self.vertices[i]
                vertex_2 = self.vertices[(i + 1) % vertices_number]
                current_perimeter += count_vertices_distance(vertex_1, vertex_2)
        return round(current_perimeter, 2)

    def __get_polygon_type(self):
        edges_number = len(self.vertices)
        previous_direction = 0

        for i in range(edges_number):
            adjacent_edges = self.__get_three_adjacent_edges(i)
            current_direction = cross_product(adjacent_edges)

            if current_direction != 0:
                if current_direction * previous_direction < 0:
                    return PolygonType.concave
                else:
                    previous_direction = current_direction

        return PolygonType.convex

    def __get_three_adjacent_edges(self, start_point_index):
        edges_number = len(self.vertices)
        first_edge = self.vertices[start_point_index]
        second_edge = self.vertices[(start_point_index + 1) % edges_number]
        third_edge = self.vertices[(start_point_index + 2) % edges_number]
        return [first_edge, second_edge, third_edge]
