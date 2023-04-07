def maxArea(self, height: list[int]) -> int:
    # Initialize two pointers, one at the beginning and one at the end of the array
    l, r = 0, len(height) - 1
    # Initialize variable to store maximum area
    res = 0

    # Continue iterating while the two pointers haven't crossed each other
    while l < r:
        # Calculate the area formed between the two lines and update 'res' if it's larger
        res = max(res, min(height[l], height[r]) * (r - l))
        # Move the pointer with the smaller height, since the larger one can't form a larger area with any other line
        if height[l] < height[r]:
            l += 1
        # If the heights are equal or the right line is smaller, move the right pointer
        elif height[r] <= height[l]:
            r -= 1
    # Return the maximum area
    return res
