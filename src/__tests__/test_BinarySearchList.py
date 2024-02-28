import pytest
import sys
import os
from BinarySearchList import bs_list

foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
def test_bs_list():
    assert bs_list(foo, 69) == True
    assert bs_list(foo, 1336) == False
    assert bs_list(foo, 69420) == True
    assert bs_list(foo, 69421) == False
    assert bs_list(foo, 1) == True
    assert bs_list(foo, 0) == False

