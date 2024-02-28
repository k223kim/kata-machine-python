import pytest
import sys
import os
from Queue import Queue

def test_queue():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(7)
    queue.enqueue(9)

    assert queue.deque() == 5
    assert queue.length == 2

    queue.enqueue(11)
    assert queue.deque() == 7
    assert queue.deque() == 9
    assert queue.peek() == 11
    assert queue.deque() == 11
    assert queue.deque() == None
    assert queue.length == 0

    queue.enqueue(69)
    assert queue.peek() == 69
    assert queue.length == 1

