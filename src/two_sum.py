#!/usr/bin/env python3

"""
Description:Given an array of integers nums and an integer target, return indices of the two numbers such that they add
up to target. You may assume that each input would have exactly one solution, and you may not use the same element
twice. You can return the answer in any order.
Author: Joseph kroon
Date: 2024-10-07

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

"""
import logging
logging.basicConfig(level=logging.INFO)

class Solution:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def two_sum(self, nums: list[int], target: int):
        try:
            assert 2 <= len(nums) <= 10 ^ 4
            assert -10 ^ 9 <= min(nums)
            assert max(nums) <= 10 ^ 9
        except AssertionError as e:
            self.logger.error(f"input out of bounds")
            raise e
        for i in nums:
            working = nums.copy()
            working.pop(i)
            for n in working:
                if i + n == target:
                    return [nums[i],nums[n]]
        else:
            return None


def main():
    print(f"hello there!")

if __name__ == "__main__":
    main()
