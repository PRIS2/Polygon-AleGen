from math import sqrt


def count_vertices_distance(vertex_1, vertex_2):
    x_distance = vertex_2.x - vertex_1.x
    y_distance = vertex_2.y - vertex_1.y
    return sqrt(x_distance * x_distance + y_distance * y_distance)


def cross_product(vector):
    x_1 = vector[1].x - vector[0].x
    y_1 = vector[1].y - vector[0].y
    x_2 = vector[2].x - vector[0].x
    y_2 = vector[2].y - vector[0].y
    return x_1 * y_2 - y_1 * x_2
