class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_len = len(nums)
        k = len(set(nums))
        ref = []
        i = 0
        while i < nums_len:
            if nums[i] not in ref:
                ref.append(nums[i])
                i=i+1
            else:
                temp = nums[i]
                nums.remove(nums[i])
                nums.append(temp)
                nums_len = nums_len - 1
        return k
