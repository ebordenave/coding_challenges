def is_permutation(strs_one: str,strs_two: str) -> bool:
    count_one, count_two = {},{}
    
    if len(strs_one) != len(strs_two):
        return False
    
    for idx in range(len(strs_one)):
        count_one[strs_one[idx]] = 1 + count_one.get(strs_one[idx], 0)
        count_two[strs_two[idx]] = 1 + count_two.get(strs_two[idx], 0)
    return count_one == count_two



strs1='tax'
strs2 ='bat'

# print(f"test 1 => \")
print(is_permutation(strs1,strs2))