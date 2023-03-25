class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Input: nums = [0,0,1,1,1,2,2,3,3,4]
        # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
        left = 0

        for right in range(1, len(nums)):
            if nums[right] != num[right-1]:
                nums[left] = nums[right]
                left += 1
        return left

print(removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))