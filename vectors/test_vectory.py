"""Testes unitários para vectory.py.

Rode com:
    python3 -m unittest test_vectory -v
"""

import unittest

from vectory import (
    dimension,
    magnitude,
    normalize,
    dot_product,
    cosine_similarity,
)


class TestVectory(unittest.TestCase):
    def test_dimension(self):
        vector = [1.0, 2.0, 3.0]

        result = dimension(vector)

        self.assertEqual(result, 3)

    def test_magnitude(self):
        pass

    def test_normalize(self):
        pass

    def test_dot_product(self):
        pass

    def test_cosine_similarity(self):
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
