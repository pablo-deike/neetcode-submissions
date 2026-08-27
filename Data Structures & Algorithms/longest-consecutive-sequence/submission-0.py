class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        diff = {}
        res = 0
        for idx, num in enumerate(nums):
            diff[num] = idx
        for num in nums:
            i = 1
            if diff.get(num - 1) is not None:
                continue
            while diff.get(num + 1) is not None:
                i += 1
                num += 1
            res = max(res, i)
        return res
