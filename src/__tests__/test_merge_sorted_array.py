import pytest
from Merge_Sorted_Array_88 import merge_sorted_array

def test_merge_sorted_array():
    arr1 = [1, 2, 3, 0, 0, 0]
    merge_sorted_array(
        arr1, 3,
        [2, 5, 6], 3
    )
    assert arr1 == [1,2,2,3,5,6]
    arr1 = [1]
    merge_sorted_array(
        arr1, 1,
        [], 0
    )
    assert arr1 == [1]
    arr1 = [0]
    merge_sorted_array(
        arr1, 0,
        [1], 1
    )
    assert arr1 == [1]
