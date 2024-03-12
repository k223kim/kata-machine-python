import pytest
from Remove_Duplicates_26 import removeDuplicates

def test_removeDuplicates():
    nums = [1, 1, 2]
    assert removeDuplicates(nums) == 2
    assert nums[:2] == [1, 2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    assert removeDuplicates(nums) == 5
    assert nums[:5] == [0,1,2,3,4]
