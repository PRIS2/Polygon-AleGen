from math import sqrt


def count_vertices_distance(vertex_1, vertex_2):
    x_distance = vertex_2.x - vertex_1.x
    y_distance = vertex_2.y - vertex_1.y
    return sqrt(x_distance * x_distance + y_distance * y_distance)
