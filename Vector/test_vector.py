import pytest
from Vector import vector


def test_default_constructor():
    vector = Vector()

    assert vector.x == 0.0
    assert vector.y == 0.0


def test_constructor():
    vector = Vector(5, 2)

    assert vector.x == 5.0
    assert vector.y == 2.0


def test_string_repr():
    assert str(Vector()) == '(0.0, 0.0)'

def test_setters():
    v = Vector()

    assert v.x == 0.0
    assert v.y == 0.0

    v.x = 5
    v.y = 6

    assert v.x == 5.0
    assert v.y == 6.0

def test_operators():
    v1, v2 = Vector(), Vector()
    v3 = Vector(3, 2)

    assert v1 == v2
    assert v1 != v3
    assert not v1 != v2
    assert not v3 == v1

def test_distance():
    p1, p2 = Vector(10, 15), Vector()

    assert p1.distance(p2) == 18.027756377319946

def test_distance_exception():
    with pytest.raises(TypeError):
        assert Vector().distance('abcde') == 18.027756377319946
