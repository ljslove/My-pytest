
from src.my_add import my_add

def test_add_one():
    result=my_add(3,4)
    assert result==7

def test_add_two():
    result=my_add(3,5)
    assert  result==8