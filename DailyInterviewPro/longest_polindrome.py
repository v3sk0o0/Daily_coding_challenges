# Pure recusion
def longest_polindrome(string):
    
    if is_polindrome(string):
        

        return string 
    left =  longest_polindrome(string[1:])
    right = longest_polindrome(string[:-1])
    
    if len(left) >= len(right):
        return left
    else:
        return right


class Solution: 
    """With cache"""
    def longestPalindrome(self, s):
        self.CACHE = dict()
        return self.longest_polindrome(s)
        
    # Fill this in.
    def is_polindrome(self,s):
    
        N = len(s)
        if N == 1:
            return s
        if N == 2 and s[0] == s[1]:
            return s
        if N == 2 and s[0] != s[1]:
            return ""

        for i in range(int(N/2 +1)):

            if s[i] != s[(N-1) - i]:
                return ""
        return s
    
    
    def longest_polindrome(self, string):

        if string in self.CACHE:
            return CACHE[string]

        if is_polindrome(string):
            return string 

        left =  longest_polindrome(string[1:])
        self.CACHE.update({string[1:] : left})

        right = longest_polindrome(string[:-1])
        self.CACHE.update({string[:-1]: right})

        if len(left) >= len(right):
            return left
        else:
            return right
    
# Test program
s = "MadamArorateachesmalayalam"
print(str(Solution().longestPalindrome(s)))
# racecar


from collections import deque

#Creating a Queue
# Naive Iterative without cache

def longest_polindrome_it(string):
    queue = deque()
    val = string
    while not is_polindrome(val):
        queue.append(val[1:])
        queue.append(val[:-1])
        val = queue.popleft()
    
    return val
# longest_polindrome_it
longest_polindrome_it("affafapoliiloplfafteachesmaaaallla")
