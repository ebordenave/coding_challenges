class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # this will hold all previous values under a specific condition
        previous_map = {}

        # create kv pairs using enum so that each value is mapped to an index
        for key, value in enumerate(nums):
            # I want to find two values that add up to a target so do the inverse operations
            diff = target - value
            # if this diff is in previous map then return the index of the difference in the previous map
            # and return the key associated with the value that resulted in the diff
            if diff in previous_map:
                return [previous_map[diff], key]
            # else previous_map at value will equal the key associated with that value
            previous_map[value] = key
        return []
        