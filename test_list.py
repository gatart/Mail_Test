import pytest
import random


def test_1(rand_list):
    a = rand_list
    x = random.randint(100, 200)
    a.append(x)
    assert a.count(x) == 1


@pytest.mark.parametrize('i', (random.randint(-100, 1), random.randint(100, 200)))
def test_2(i, rand_list):
    with pytest.raises(ValueError):
        assert rand_list.remove(i)


def test_3(rand_list):
    a = rand_list.copy()
    assert a == rand_list
