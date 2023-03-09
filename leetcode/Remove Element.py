class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_len = len(nums)
        i = 0
        while i < nums_len:
            if nums[i] != val:
                i=i+1
            else:
                temp = nums[i]
                nums.remove(nums[i])
                nums.append(temp)
                nums_len = nums_len - 1
        return nums_len
