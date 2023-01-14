#input = nums = [3,2,2,3]
# val = 3


def removeElement(self, nums: list[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
            
removeElement(5,nums=[8,9,2,3,5],val=1)

