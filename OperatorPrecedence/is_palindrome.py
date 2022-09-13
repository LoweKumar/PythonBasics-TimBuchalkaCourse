def palindrome(word_check):
    return word_check[::-1].casefold() == word_check.casefold()

def palindrome_sentence(sentence_check):
    string = ""
    for char in sentence_check:
        if char.isalnum():
            string+= char
    print(string)
    return palindrome(string)

# Sentence to check :"do geese see god"
sentence = input("Enter the Sentence to check for palindrome")
if palindrome_sentence(sentence):
    print("{0} is palindrome".format(sentence))
else:
    print("{0} is not palindrome".format(sentence))