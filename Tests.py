import unittest
from Polygon import Polygon
from PolygonType import PolygonType
from Utils import count_vertices_distance
from Vertex import Vertex


class VerticesDistanceTests(unittest.TestCase):

    def test_1(self):
        vertex_1 = Vertex(0, 0)
        vertex_2 = Vertex(0, 5)
        result = count_vertices_distance(vertex_1, vertex_2)
        expected_result = 5

        self.assertEqual(result, expected_result)

    def test_2(self):
        vertex_1 = Vertex(14, 5)
        vertex_2 = Vertex(2, 5)
        result = count_vertices_distance(vertex_1, vertex_2)
        expected_result = 12

        self.assertEqual(result, expected_result)

    def test_3(self):
        vertex_1 = Vertex(3, 0)
        vertex_2 = Vertex(-9, 5)
        result = count_vertices_distance(vertex_1, vertex_2)
        expected_result = 13

        self.assertEqual(result, expected_result)


class PolygonTypeTests(unittest.TestCase):

    def test_1(self):
        vertex_1 = Vertex(0, 0)
        vertex_2 = Vertex(0, 1)
        vertex_3 = Vertex(1, 1)
        vertex_4 = Vertex(1, 0)
        vertices = [vertex_1, vertex_2, vertex_3, vertex_4]

        polygon = Polygon(vertices)
        result = polygon.type
        expected = PolygonType.convex

        self.assertEqual(result, expected)

    def test_2(self):
        vertex_1 = Vertex(1.5, 1.5)
        vertex_2 = Vertex(0, 2)
        vertex_3 = Vertex(2, 2)
        vertex_4 = Vertex(2, 0)
        vertices = [vertex_1, vertex_2, vertex_3, vertex_4]

        polygon = Polygon(vertices)
        result = polygon.type
        expected = PolygonType.concave

        self.assertEqual(result, expected)

    def test_3(self):
        vertex_1 = Vertex(-2, -4)
        vertex_2 = Vertex(6, -1)
        vertex_3 = Vertex(6, 5)
        vertex_4 = Vertex(0, 8)
        vertex_5 = Vertex(-5, 3)
        vertices = [vertex_1, vertex_2, vertex_3, vertex_4, vertex_5]

        polygon = Polygon(vertices)
        result = polygon.type
        expected = PolygonType.convex

        self.assertEqual(result, expected)


class PolygonPerimeterTests(unittest.TestCase):

    def test_1(self):
        vertex_1 = Vertex(0, 0)
        vertex_2 = Vertex(0, 1)
        vertex_3 = Vertex(1, 1)
        vertex_4 = Vertex(1, 0)
        vertices = [vertex_1, vertex_2, vertex_3, vertex_4]

        polygon = Polygon(vertices)
        result = polygon.perimeter
        expected = 4

        self.assertEqual(result, expected)

    def test_2(self):
        vertex_1 = Vertex(-2, -4)
        vertex_2 = Vertex(6, -1)
        vertex_3 = Vertex(6, 5)
        vertex_4 = Vertex(0, 8)
        vertex_5 = Vertex(-5, 3)
        vertices = [vertex_1, vertex_2, vertex_3, vertex_4, vertex_5]

        polygon = Polygon(vertices)
        result = polygon.perimeter
        expected = 35.94

        self.assertEqual(result, expected)
