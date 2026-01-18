"""
LeetCode 0080: Remove Duplicates from Sorted Array II
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
Difficulty: Medium
Category: Two Pointers

Pattern:
- Two pointers (slow / fast)

Key Idea:
- Allow each number to appear at most twice
- Use slow pointer to track write position
- Compare current number with nums[slow - 2]

Edge Cases:
- Array length <= 2
- All elements same

Complexity:
- Time: O(n)
- Space: O(1)
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        slow = 2
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        return slow
