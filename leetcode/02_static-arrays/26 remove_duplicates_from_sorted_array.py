class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # begin head pointer at 1 as a count
        head = 1
        
        # iterate through the arr starting at 1
        for tail in range(1, len(nums)):
            
            # as you iterate, check the curr value against the previous value in the arr
            # if the match, move on to the next, if it is unique, add to arr called nums
            if nums[tail] != nums [tail-1]:
                nums[head] = nums [tail]
                # move the head pointer by 1
                head += 1
        # return the head value so that the count output is counting all the unique values in the arr
        return head
    
nums = [0,0,1,1,1,2,2,3,3,4]