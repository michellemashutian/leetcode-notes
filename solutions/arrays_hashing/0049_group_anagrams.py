"""
LeetCode 49: Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Difficulty: Medium
Category: Arrays & Hashing

Pattern:
- Hash Table

Key Idea:
- 每个单词用sorted(单词)，对每个单词的字母进行排序，返回一个新的列表，sorted("python") 返回的是一个列表 ['h', 'n', 'o', 'p', 't', 'y']
- 然后这个列表连起来，就是这个单词的key,单词是value，存储到dict中，最后返回dict的values()

Complexity:
- n = strs 中字符串的数量，k = strs 中最长字符串的长度
- Time: The time complexity is O(nk log k), where n is the number of strings and k is the maximum length of a string. 
We iterate through all n strings and sort each string, which takes O(k log k) time. Therefore, the overall time complexity is O(nk log k).
- Space: The space complexity is O(nk) because the hash map can store up to n unique keys, and each key can contain up to k characters.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_dict = {}
        for str_word in strs:
            str_key = "".join(sorted(str_word))
            if str_key in str_dict:
                str_dict[str_key].append(str_word)
            else:
                str_dict[str_key] = [str_word]
        return list(str_dict.values())

"""
Key Idea:
- 每个单词count包含字母的个数，这个count列表就是单词的key,单词是value

Complexity:
- n = strs 中字符串的数量，k = strs 中最长字符串的长度
- Time: The time complexity is O(nk), where n is the number of strings and k is the maximum string length. 
We iterate through each string and count the frequency of each character.
- Space: The space complexity is O(n), because we store at most n groups in a hash map. Each key is a fixed-size tuple of 26 integers, so it takes constant space.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_dict = {}
        for str_word in strs:
            count = [0] *26
            for char in str_word:
                index = ord(char) - ord("a")
                count[index]+=1
            str_key = tuple(count)
            if str_key in str_dict:
                str_dict[str_key].append(str_word)
            else:
                str_dict[str_key] = [str_word]
        return list(str_dict.values())

