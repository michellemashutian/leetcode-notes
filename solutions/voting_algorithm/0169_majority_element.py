"""
LeetCode 0169: Majority Element
Link: https://leetcode.com/problems/majority-element/
Difficulty: Easy
Category: voting_algorithm

Pattern:
- e.g. Sliding Window / Two Pointers / DFS / DP

Key Idea:
- 维护两个变量：
  - candidate：当前候选的多数元素
  - count：候选元素的票数
- 遍历数组：
  - 如果 count == 0，说明当前没有候选人，将当前元素设为 candidate
  - 如果当前元素等于 candidate，count += 1
  - 否则 count -= 1
- 遍历结束后，candidate 即为多数元素

Edge Cases:
- 数组长度为 1
- 所有元素都相同
- 多数元素分布在数组任意位置（开头 / 中间 / 结尾）

Complexity:
- Time: O(n)
- Space: O(1)
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count+=1
            else:
                count-=1
        return candidate

