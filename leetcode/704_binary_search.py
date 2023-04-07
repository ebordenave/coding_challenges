def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1  # Initialize pointers to the leftmost and rightmost indices of the array

    while l <= r:  # While there is still a subarray to search
        m = l + ((r - l) // 2)  # Calculate the middle index of the subarray to check
                                # The use of // instead of / ensures integer division
                                # This prevents a floating point result and avoids rounding errors
                                # The formula for m also avoids overflow, unlike (l + r) // 2
        if nums[m] > target:  # If the middle element is greater than the target
            r = m - 1  # Discard the right half of the subarray
        elif nums[m] < target:  # If the middle element is less than the target
            l = m + 1  # Discard the left half of the subarray
        else:  # If the middle element is equal to the target
            return m  # Return the index of the target element
