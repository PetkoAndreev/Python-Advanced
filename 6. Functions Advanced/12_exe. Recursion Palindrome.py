def palindrome(word, index=0):
    if len(word) < 2 or word[0] == word[-1] and palindrome(word[1:-1]):
        return f'{word} is a palindrome'
    return f'{word} is not a palindrome'

print(palindrome("abcba", 0))



