class Solution(object):
    def searchInsert(self, nums, target):
     
        if target > nums[-1]:
            return len(nums)

        for i in range(len(nums)):
            if nums[i] == target:
                break
            elif nums[i] > target:
                break
            
        return i