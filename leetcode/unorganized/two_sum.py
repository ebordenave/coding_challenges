# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_map = {}
        for k, v in enumerate(nums):
            difference = target - v
            if difference in previous_map:
                return [previous_map[difference], k]
            previous_map[v] = k
        return
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # initialize a dictionary
#         prevMap = {}  # val : index
#
#         # key value pairs and enumerating the numbers in the list
#         for i, j in enumerate(nums):
#             # taking the target answer, subtract the nums, this will be assigned to the diff
#             diff = target - nums
#             # if that difference is in the dictionary, return that diff val and its index
#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[j] = i
#         return

# enumerate method keeps count of iterations, using indices
# it can accept an argument to start the index with another number as its 1 count
