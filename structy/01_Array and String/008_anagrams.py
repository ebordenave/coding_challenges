# def anagrams(s1, s2):
#     return char_count(s1) == char_count(s2)
#     pass


# def char_count(s):
#     count = {}
    
#     for char in s:
#         if char not in count:
#             count[char] = 0
#         count[char] += 1
#     return count

# s1 = 'rats'
# s2 = 'star'

# print(anagrams(s1,s2))

def pop_first(self, value):
    if self.length == 0:
        return None
    
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1


        