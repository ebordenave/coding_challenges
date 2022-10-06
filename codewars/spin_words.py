# Write a function that takes in a string of one or more words, and returns the same string, but with all five or
# more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and
# spaces. Spaces will be included only when more than one word is present.
import string


# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    new_str = ''
    for word in sentence.split():
        if len(word) < 5:
            new_str += word + ' '
        elif len(word) >= 5:
            new_str += word[::-1] + ' '
    new_str = new_str[:-1]
    print(new_str)
    return new_str


spin_words('Welcome is another test')
# # best solution
# def spin_words(sentence):
#     # Your code goes here
#     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
