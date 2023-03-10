from ting_file_management.priority_queue import PriorityQueue
import pytest


# task 6 - thiago guarino
def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    num1_preference = {'qtd_linhas': 2}
    num2_preference = {'qtd_linhas': 3}
    num3_preference = {'qtd_linhas': 4}
    num1_non_preference = {'qtd_linhas': 7}
    num2_non_preference = {'qtd_linhas': 5}
    num3_non_preference = {'qtd_linhas': 11}
    num4_non_preference = {'qtd_linhas': 9}

    priority_queue.enqueue(num4_non_preference)
    priority_queue.enqueue(num3_preference)
    priority_queue.enqueue(num1_preference)
    priority_queue.enqueue(num2_non_preference)
    priority_queue.enqueue(num1_non_preference)
    priority_queue.enqueue(num3_non_preference)
    priority_queue.enqueue(num2_preference)
    assert len(priority_queue) == 7

    assert priority_queue.search(0) == num3_preference
    assert priority_queue.search(1) == num1_preference
    assert priority_queue.search(2) == num2_preference
    assert priority_queue.search(3) == num4_non_preference
    assert priority_queue.search(4) == num2_non_preference
    assert priority_queue.search(5) == num1_non_preference
    assert priority_queue.search(6) == num3_non_preference

    with pytest.raises(IndexError):
        priority_queue.search(-1)
    with pytest.raises(IndexError):
        priority_queue.search(10)

    assert priority_queue.dequeue() == num3_preference
    assert priority_queue.dequeue() == num1_preference
    assert priority_queue.dequeue() == num2_preference
    assert priority_queue.dequeue() == num4_non_preference
    assert priority_queue.dequeue() == num2_non_preference
    assert priority_queue.dequeue() == num1_non_preference
    assert priority_queue.dequeue() == num3_non_preference
    assert len(priority_queue) == 0
