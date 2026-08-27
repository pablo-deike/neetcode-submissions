class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_map = {}
        for i in range(len(nums)):
            print(i)
            difference = target - nums[i]
            if difference_map.get(difference) is None:
                difference_map[nums[i]] = i
            else:
                return [difference_map[difference], i]

