"""
LeetCode 0080: Remove Duplicates from Sorted Array II
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
Difficulty: Medium
Category: two_pointers

Pattern:
- 双指针（快慢指针）

Key Idea:
- 数组已经排序，相同的元素一定是连续出现的。
- 本题允许每个元素最多出现两次。
- 使用快慢指针在原数组上进行原地修改（in-place）。
- 慢指针 slow 表示当前可以写入的位置（即结果数组的长度）。
- 快指针 fast 从左到右遍历数组。
- 对于当前 nums[fast]：
  - 如果 slow < 2，说明前面元素不足两个，直接保留；
  - 如果 slow >= 2：
    - 只要 nums[fast] != nums[slow - 2]，就可以保留当前元素；
    - 否则说明该元素已经出现至少两次，跳过。
- 最终 slow 即为处理后数组的有效长度 k。

Edge Cases:
- 数组长度小于等于 2，直接返回原长度
- 所有元素都相同
- 所有元素都不同
- 恰好每个元素出现两次

Complexity:
- Time: O(n)，只遍历一次数组
- Space: O(1)，原地修改，不使用额外空间

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
