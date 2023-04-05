class Solution:
    def threeSum(self, integers: list[int]) -> list[list[int]]:
        # sort the integers and create a list called result
        integers.sort()
        result = []
        
        # for loop iteration through the integers and if the value at index is greater than 0
        for index in range(len(integers)):
            if integers[index] > 0:
                break
            if index > 0 and integers[index] == integers[index - 1]:
                continue
            left, right = index + 1, len(integers) - 1
            
        # while left and rigth are not empty, if the int at left plus the int at right are less than 0 -- int at index, add left
            while left < right:
                if integers[left] + integers[right] < 0 - integers[index]:
                    left += 1
                elif integers[left] + integers[right] > 0 - integers[index]:
                    right -= 1
                else:
                    result.append([integers[index], integers[left], integers[right]]) # After a triplet is appended, we try our best to incease the numeric value of its first element or that of its second.
                    left += 1 # The other pairs and the one we were just looking at are either duplicates or smaller than the target.
                    right -= 1 # The other pairs are either duplicates or greater than the target.
                    # We must move on if there is less than or equal to one integer in between the two integers.
                    while integers[left] == integers[left - 1] and left < right:
                        left += 1 # The pairs are either duplicates or smaller than the target.
        return result
