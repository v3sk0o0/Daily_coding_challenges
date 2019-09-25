
# Given a string, find the length of the longest substring without repeating characters.


class Solution:
    
    def lengthOfLongestSubstring(self, s):

        current = 0
        longest = 0
        cache = dict()
        for letter in s:
            
            if letter in cache:
                longest = max(current, longest)
                cache = dict({letter: letter})
                current = 1
            else:
                current += 1
                cache.update({letter : letter})
        return longest

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))

