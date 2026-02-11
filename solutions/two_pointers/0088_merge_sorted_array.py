"""
LeetCode 0088: Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/
Difficulty: Easy
Category: two_pointers

Pattern:
- Two Pointers (from the end) + In-place merge

Key Idea:
- nums1 的后面有足够的 0 作为“空位”，所以不要从前往后合并（会覆盖 nums1 里还没用到的元素）。
- 正确做法：从后往前填。
  - p1 指向 nums1 有效部分最后一个元素（m-1）
  - p2 指向 nums2 最后一个元素（n-1）
  - p 指向 nums1 最后一个位置（m+n-1）
- 每次比较 nums1[p1] 和 nums2[p2]：
  - 谁更大，就把谁放到 nums1[p]，然后对应指针左移
  - p 左移
- 当 p2 < 0 时结束：说明 nums2 全部放进去了，nums1 剩下的本来就在正确位置，不用动
- 若 p1 < 0 但 p2 仍有剩：把 nums2 的剩余前缀拷贝进 nums1[0..p2]

Edge Cases:
- n == 0：nums2 为空，nums1 不用改
- m == 0：nums1 有效部分为空，直接把 nums2 全部拷贝到 nums1
- 全部元素都来自 nums2（nums1 前半用完很快）
- 大量重复元素（比较时用 >= 或 > 都可以，只要保证指针更新正确）
- nums1 / nums2 已经有序但一边完全小于另一边（例如 nums1 全小、nums2 全大）

Complexity:
- Time: O(m + n)  （每个元素最多比较/移动一次）
- Space: O(1)     （原地合并，不用额外数组）
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # 指向 nums1 有效部分末尾
        p1 = m - 1
        # 指向 nums2 末尾
        p2 = n - 1
        # 指向 nums1 最后一个位置
        p = m + n - 1

        # 从后往前合并
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # 如果 nums2 还有剩余，拷贝到 nums1 前面
        # （nums1 剩余的不需要管，本来就在正确位置）
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

