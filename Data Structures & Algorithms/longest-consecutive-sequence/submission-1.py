class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        res = 0
        for num in nums:
            num_set.add(num)
        for num in nums:
            i = 1
            if num - 1 in num_set:
                continue
            while num + 1 in num_set:
                i += 1
                num += 1
            res = max(res, i)
        return res
