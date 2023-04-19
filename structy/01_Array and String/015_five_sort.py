def five_sort(nums):
    l = 0
    r = len(nums)-1

    while l < r:
        if nums[r] == 5:
            r -= 1
        elif nums[l] == 5:
            nums[l],nums[r] = nums[r], nums[l]
            l += 1
        else:
            l += 1
    return nums