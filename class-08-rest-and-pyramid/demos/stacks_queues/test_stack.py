from .stack import Stack
import pytest


@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def small_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    return stack


def test_stack_class_exists():
    assert Stack


def test_can_instantiate_empty_stack(empty_stack):
    assert isinstance(empty_stack, Stack)


def test_insertion_of_value_increases_len(empty_stack):
    assert len(empty_stack) == 0
    empty_stack.push(100)
    assert len(empty_stack) == 1


def test_default_value_of_top(empty_stack):
    assert empty_stack.top is None

