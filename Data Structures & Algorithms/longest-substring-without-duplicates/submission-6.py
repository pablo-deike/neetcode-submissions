class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        seen_characters = set()
        last_seen_index = 1
        for right in range(len(s)):
            while s[right] in seen_characters:
                seen_characters.remove(s[left])
                left += 1
            seen_characters.add(s[right])
            last_seen_index = max(right - left + 1, last_seen_index)
        return last_seen_index
