import unittest
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
