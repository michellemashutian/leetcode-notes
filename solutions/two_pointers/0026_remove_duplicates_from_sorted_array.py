"""
LeetCode 0026: Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Difficulty: Easy
Category: two_pointers

Pattern:
- 双指针（快慢指针）

Key Idea:
- 数组已经是有序的，相同元素一定是连续出现的。
- 使用快慢指针在原数组上原地去重（in-place）。
- 慢指针 slow 表示当前已处理好的「不重复元素」的最后位置。
- 快指针 fast 从第二个元素开始遍历数组。
- 当 nums[fast] != nums[slow] 时：
  - 说明遇到了一个新的不重复元素
  - 将其写入 nums[slow + 1]
  - slow 向前移动一位
- 遍历结束后，前 slow + 1 个元素即为去重后的结果。

Edge Cases:
- 空数组，直接返回 0
- 数组长度为 1，直接返回 1
- 所有元素都相同
- 所有元素都不相同

Complexity:
- Time: O(n)，只遍历一次数组
- Space: O(1)，原地修改，不使用额外空间

"""

from typing import List, Optional
from collections import defaultdict, deque


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow+1

    '''
        if not nums:
            return 0
        
        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast-1] != nums[fast]:     
                nums[slow] = nums[fast]
                slow += 1
        return slow
        
    '''

