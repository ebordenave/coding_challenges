# class Solution:
#     def __init__(self, ransomNote, magazine):
#         self.ransomNote = ransomNote
#         self.magazine = magazine
#
#     def get_ransomNote(self):
#         return self.ransomNote
#
#     def get_magazine(self):
#         return self.magazine

def canConstruct(ransomNote: str, magazine: str) -> bool:
    for _ in magazine:
        if _ not in ransomNote:
            return False


canConstruct(ransomNote='aa', magazine='ab')
