class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, sum(nums)

        for k,v in enumerate(nums):
            rightSum -= v
            if leftSum == rightSum:
                return k
            else:
                leftSum += v
        return -1
            
        