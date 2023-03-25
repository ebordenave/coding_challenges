def pivotIndex(self, nums):
    leftSum, rightSum = 0, sum(nums)
    # This loop iterates through each element in the nums list, 
    # keeping track of the index of each element (idx) and the 
    # value of each element (ele).
    for idx, ele in enumerate(nums):
        # The rightSum variable is updated by subtracting the 
        # current element (ele) from it. This effectively 
        # calculates the sum of all elements to the right of the current index.
        rightSum -= ele
        # The if statement checks if the sum of all 
        # elements to the left of the current index 
        # (leftSum) is equal to the sum of all elements 
        # to the right of the current index (rightSum). 
        # If they are equal, then the current index 
        # is the pivot index, so the function returns idx.
        if leftSum == rightSum:
            return idx
        leftSum += ele
    return -1