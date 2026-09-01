class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''.join(filter(str.isalnum, s.lower()))
        return res == res[::-1]