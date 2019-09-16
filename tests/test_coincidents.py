from timing_neighbors.coincidents import coincident_indices
from timing_neighbors.coincidents import coincidents


delta = 0.1


def setup_0():
    """Setup test 0."""
    list0 = [i for i in range(10)]
    list1 = [i + 0.5 for i in range(20)]
    list1[5] = 5
    return list0, list1


def test_coincident_indices_0():
    """Simple test with one coincident time."""
    list0, list1 = setup_0()

    solution = {5: 5}
    assert coincident_indices(list0, list1, delta) == solution


def test_coincidents_0():
    """Simple test with one coincident time."""
    list0, list1 = setup_0()
    indices = coincident_indices(list0, list1, delta)

    solution = {5: 5}
    assert coincidents(list0, list1, indices) == solution


def setup_1():
    """Setup test 1."""
    list0 = [i for i in range(10)]
    list1 = [i + 0.5 for i in range(5, 20)]
    list1[3] = 8
    return list0, list1


def test_coincident_indices_1():
    """Test with different indices."""
    list0, list1 = setup_1()

    solution = {8: 3}
    assert coincident_indices(list0, list1, delta) == solution


def test_coincidents_1():
    """Test with different indices."""
    list0, list1 = setup_1()
    indices = coincident_indices(list0, list1, delta)

    solution = {8: 8}
    assert coincidents(list0, list1, indices) == solution


def setup_2():
    """Setup test 2."""
    list0 = [i for i in range(20)]
    list1 = [i + 0.5 for i in range(10, 30)]
    list1[3] = 13
    list1[8] = 18
    return list0, list1


def test_coincident_indices_2_0():
    """Test with two coincident indices."""
    list0, list1 = setup_2()

    solution = {13: 3, 18: 8}
    assert coincident_indices(list0, list1, delta) == solution


def test_coincident_indices_2_1():
    """Test with two coincident indices for one item."""
    list0, list1 = setup_2()
    list1[4] = 13.1

    solution = {13: 3, 18: 8}
    assert coincident_indices(list0, list1, delta) == solution


def test_coincidents_2():
    """Test with two coincident indices."""
    list0, list1 = setup_2()
    indices = coincident_indices(list0, list1, delta)

    solution = {13: 13, 18: 18}
    assert coincidents(list0, list1, indices) == solution
