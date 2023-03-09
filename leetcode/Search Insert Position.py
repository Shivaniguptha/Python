class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
            
        else:
            if (nums[0] > target):
                    return 0
            for i in range(0, len(nums)-1):
                if ((nums[i] < target) and (nums[i+1] > target)):
                    return (i+1)
            return (len(nums))
