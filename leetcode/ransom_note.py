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
    TrueOrFalse = 0
    for _ in magazine:
        # print(_)
        if _ not in ransomNote:
            TrueOrFalse -= 1
        else:
            TrueOrFalse += 1
    if TrueOrFalse > 0:
        return True
    else:
        return False


canConstruct(ransomNote='aa', magazine='ab')
