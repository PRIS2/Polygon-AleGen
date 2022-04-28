from Polygon import Polygon
from Vertex import Vertex

if __name__ == '__main__':
    vertex_1 = Vertex(-2, -4)
    vertex_2 = Vertex(6, -1)
    vertex_3 = Vertex(6, 5)
    vertex_4 = Vertex(0, 8)
    vertex_5 = Vertex(-5, 3)
    vertices = [vertex_1, vertex_2, vertex_3, vertex_4, vertex_5]

    polygon = Polygon(vertices)
