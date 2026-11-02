from math import sqrt;

def dimension(v: list[float]) -> int:
    return len(v)

def magnitude(v: list[float]) -> float:
    return sqrt(sum(x ** 2 for x in v))

def normalize(v: list[float]) -> list[float]:
    mag = magnitude(v)
    return [x / mag for x in v]

def dot_product(v1: list[float], v2: list[float]) -> float:
    if len(v1) != len(v2):
        raise ValueError("Dimensões incompatíveis")
    return sum(x * y for x, y in zip(v1, v2))

def cosine_similarity(v1: list[float], v2: list[float]) -> float:
    denominator = magnitude(v1) * magnitude(v2)
    if denominator == 0:
        raise ValueError("Vetor nulo")
    return dot_product(v1, v2) / denominator