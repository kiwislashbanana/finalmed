import pytest
from median import mediana

def test_correct_lists_even():
    assert mediana([1, 2], [3, 4]) == 2.5

def test_correct_lists_odd():
    assert mediana([1, 3], [2]) == 2

def test_non_list_input():
    with pytest.raises(TypeError):
        mediana(2, [1, 2])
    
def test_empty_lists():
    with pytest.raises(ValueError):
        mediana([], [])
        
def test_one_empty_list():
    assert mediana([], [1]) == 1
    assert mediana([2], []) == 2

def test_unsorted_lists():
    assert mediana([3, 1], [4, 2]) == 2.5