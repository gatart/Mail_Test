import pytest
import random


def test_1():
    a = tuple()
    assert a == ()


@pytest.mark.parametrize('i', (random.randint(-100, 1), 10, random.randint(100, 200)))
def test_2(i, rand_list):
    a = rand_list
    a.append(10)
    b = tuple(a)
    with pytest.raises(AttributeError):
        assert b.remove(i)


def test_3():
    a = random.randint(1, 10)
    b = (1, 1)
    b *= a
    assert b.count(1) == a * 2
