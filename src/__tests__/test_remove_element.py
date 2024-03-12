import pytest
from Remove_Element_27 import removeElement

def test_removeElement():
    nums = [3, 2, 2, 3]
    assert removeElement(nums, 3) == 2
    assert nums[:2] == [2, 2]
    nums = [0,1,2,2,3,0,4,2]
    assert removeElement(nums, 2) == 5
    assert nums[:5] == [0,1,3,0,4]
