class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return min(nums[0], nums[1])
        j = n // 2
        print(j, n)
        pivot = nums[j]
        if nums[j - 1] > pivot:
            return pivot
        elif nums[(j + 1) % n] < pivot:
            return nums[(j + 1) % n]
        return min(self.findMin(nums[:j]), self.findMin(nums[j:]))
        