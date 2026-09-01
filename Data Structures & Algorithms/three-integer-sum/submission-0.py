class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            target = -nums[i]
            while l < r:
                two_sum = nums[l] + nums[r]
                if two_sum < target:
                    l += 1
                elif two_sum > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l-1] == nums[l]:
                        l += 1
                    while l<r and nums[r+1] == nums[r]:
                        r -= 1
        return res
            