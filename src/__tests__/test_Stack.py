import pytest
from Stack import Stack

def test_stack():
    stack = Stack()
    stack.push(5)
    stack.push(7)
    stack.push(9)

    assert stack.pop() == 9
    assert stack.length == 2

    stack.push(11)
    assert stack.pop() == 11
    assert stack.pop() == 7
    assert stack.peek() == 5
    assert stack.pop() == 5
    assert stack.pop() == None
    assert stack.length == 0

    stack.push(69)
    assert stack.peek() == 69
    assert stack.length == 1

