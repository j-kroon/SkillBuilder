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

    def build_list(self, nums: list[int], target):
        combos = []
        for i in range(int(target/2+1)):
            combo = [i, target-i]
            for x in combo:
                if x == combo[1]:
                    if nums.count(x) > 1:
                        piece1 = nums.index(x)
                        piece2 = nums.index(x,x)
                    else:
                        return None
                    return [piece1, piece2]
                else:
                    iterable_nums = iter(nums)
                    if all(item in iterable_nums for item in combo):
                        piece1 = nums.index(combo[0])
                        piece2 = nums.index(combo[1])
                        return ()
        return combos

    def two_sum(self, nums: list[int], target: int):
        try:
            assert 2 <= len(nums) <= 10**4
            assert -10**9 <= min(nums)
            assert max(nums) <= 10**9
        except AssertionError as e:
            raise e
        exploded = [lambda:x for x in target]
        for i in nums:
            for n in nums[:i]:
                if nums[i] + nums[n] == target:
                    return [i,n]
            for n in nums[i:]:
                if nums[i] + nums[n] == target:
                    return [i,n]
        else:
            return None


def main():
    print(f"hello there!")

if __name__ == "__main__":
    main()
