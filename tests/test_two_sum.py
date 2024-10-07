from logging import ERROR
from pytest import raises

from src.two_sum import Solution

def test_two_sum_with_answer():
    """
    only one valid answer exists
    may not use same element twice
    :return:
    """
    sol = Solution()
    numbers = [0,1,3]
    target = 1
    result = sol.two_sum(nums=numbers, target=target)
    assert result == [0,1]
    assert 2 <= len(numbers) <= 10^4
    assert -10^9 <= min(numbers)
    assert max(numbers) <= 10^9

def test_two_sum_bad_input():
    sol = Solution()
    numbers = [0,1,5,6,100000000000000000000]
    target = 200

    with raises(AssertionError) as e_info:
        sol.two_sum(nums=numbers, target=target)