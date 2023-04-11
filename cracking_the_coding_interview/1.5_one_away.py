def is_one_edit_away(s: str,t: str) -> bool:
    edit_count = 0
    
    if len(s) != len(t):
        edit_count += abs(len(s) - len(t))
        print(edit_count)
    

    # this determines edits by chars not matching between strings
    for idx in range(min(len(s), len(t))):
        if s[idx] != t[idx]:
            edit_count += 1
        print(edit_count)
    
        
    if edit_count > 1:
        return False
    return True


string_one = 'pale'
string_two = 'ple'


print(is_one_edit_away(string_one,string_two))

# class Solution:
#     def isOneEditDistance(self, s: str, t: str) -> bool:
#         if abs(len(s)-len(t))>=2 or t==s:
#             return False
        
#         s_pointer,t_pointer=0,0        
#         Flag=False
        
#         while s_pointer<len(s) and t_pointer<len(t):
#             if s[s_pointer]!=t[t_pointer]:
#                 if not Flag: #this is the first time a character is found different
#                     Flag=True
#                 else:
#                     #found more than 1 character different return False
#                     return False
#                 if len(s)>=len(t):
#                     s_pointer+=1
#                 if len(s)<=len(t):
#                     t_pointer+=1
                    
#             else:
#                 s_pointer+=1
#                 t_pointer+=1
                
#         return True

