"""
LeetCode 0027: Remove Element
Link: https://leetcode.com/problems/remove-element/
Difficulty: Easy
Category: two_pointers

Pattern:
- Two Pointers（快慢指针）+ In-place

Key Idea:
- 使用快慢指针在原数组上进行原地修改（in-place）。
- 快指针 fast 从左到右遍历数组中的每一个元素。
- 慢指针 slow 指向当前应该存放「不等于 val 的元素」的位置。
- 当 nums[fast] != val 时：
  - 将 nums[fast] 覆盖写入 nums[slow]
  - slow 向前移动一位
- 遍历结束后，slow 即为不等于 val 的元素个数 k。
- 下标 [0, k-1] 的元素均为有效结果，其余部分无需关心。

Edge Cases:
- 空数组，直接返回 0
- 所有元素都等于 val，返回 0
- 数组中没有 val，返回原数组长度
- 数组只有一个元素

Complexity:
- Time: O(n)，只遍历一次数组
- Space: O(1)，原地修改，不使用额外空间

"""

from typing import List, Optional
from collections import defaultdict, deque


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 慢指针，指向下一个可写入的位置
        slow = 0
        # 快指针遍历数组
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow

