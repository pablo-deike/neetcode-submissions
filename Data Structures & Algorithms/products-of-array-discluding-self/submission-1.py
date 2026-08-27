class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suf = [1] * n
        for i in range(n - 1):
            pref[i + 1] = pref[i] * nums[i]
            suf[n - i - 2] = suf[n - i - 1] * nums[n - i - 1]
        return [suf[i] * pref[i] for i in range(n)]