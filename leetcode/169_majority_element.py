# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:


def majorityElement(nums: list[int]) -> int:
    curr, count = nums[0], 1
    
    for num in nums:
        # add 1 to the count if the current majority element is equal to num otherwise subtract 1
        count += (1 if curr == num else -1)
        # if count is zero, then the current is number is equal to num and its count is back at 1
        if not count:
            curr = num
            count = 1
    # print the majority element
    return print(curr)
    

    
nums = [3,2,3]

majorityElement(nums)