num = [1,1,2,1,6,3,8,8,1]

def count_good_tuples(src_list: list) -> int:
    count = 0
    
    for i in range(len(src_list)-2):
        sliding_window = (src_list[i],src_list[i+1],src_list[i+2])
        if is_good_tuple(sliding_window) == True:
            count += 1
    # print(count)
    return count
        
def is_good_tuple(t: tuple) -> bool:
    
    if t[0] == t[1] and t[0] == t[2] and t[1] == t[2]:
        return False
    elif t[0] != t[1] and t[0] != t[2] and t[1] != t[2]:
        return False
    else:
        return True
    
tp = (1,1,2)
print(count_good_tuples(num))

# print(f"this should be true => {is_good_tuple((1,1,2))}")
# print(f"this should be false => {is_good_tuple((1,1,1))}")
# print(f"this should be false => {is_good_tuple((1,8,9))}")
# print(f"this should be true => {is_good_tuple((1,2,2))}")
# print(f"this should be true => {is_good_tuple((1,2,1))}")



    
count_good_tuples(num)