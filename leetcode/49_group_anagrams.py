def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # Create an empty dictionary to store groups of anagrams
    dic={}

    # Iterate over each word in the input list of strings
    for word in strs:
        # Sort the letters in the word alphabetically and join them back into a string
        sortedword = "".join(sorted(list(word)))

        # If the sorted word is not already a key in the dictionary, add it with the word as the value
        if sortedword not in dic:
            dic[sortedword]=[word]
        # Otherwise, append the word to the existing list of words associated with the sorted word
        else:
            dic[sortedword].append(word)
    
    # Return a list of lists containing the values in the dictionary (i.e., the groups of anagrams)
    return print([i for i in dic.values()])

# Call the groupAnagrams function with an example input
groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])