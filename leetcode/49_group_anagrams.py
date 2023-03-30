
def groupAnagrams( strs: list[str]) -> list[list[str]]:
    # create a dictionary     
    dic={}

    # for word in strings, create a var with the values of the sorted word, also put this word in a list
    # if the sorted word is not in the dictionary, we add it dic[sortedword]=[word]
    # else dic[sortedword] and we append word

    for word in strs:
        #this creates a sorted
        sortedword= "".join(sorted(list(word)))


        if sortedword not in dic:
            dic[sortedword]=[word]
            # print(dic)

        else:
            dic[sortedword].append(word)
    
    return print([i for i in dic.values()])

groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])




