import pytest
import random


@pytest.fixture()
def rand_list():
    yield [random.randint(1, 100) in range(5)]
