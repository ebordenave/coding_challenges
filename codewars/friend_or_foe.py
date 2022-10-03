# Make a program that filters a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be
# sure he's not...
# # Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

def friend(ls):
    friends_list = []
    for name in ls:
        if len(name) == 4:
            friends_list.append(name)
    return friends_list


# 1 loop through items in list
# 2 if length of name equals 4
# 3 append to friends list
# 4 return friends list

# best solution ->
# def friend(x):
#     return [name for name in ls if len(name) == 4]

