import pytest
import source.my_fucntions as my_functions

def test_add():
    result = my_functions.add(1,2)
    assert result == 3

def test_divide():
    result = my_functions.divide(3, 3)
    assert  result == 1

def test_divide_by_zero():
   with pytest.raises(ZeroDivisionError):
       my_functions.divide(2, 0)


def test_add_strings():
    result = my_functions.add("i like", 'burgers')
    assert result == 'i likeburgers'













