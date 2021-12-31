#Write a method is_palindrome(word) that takes in a string word and returns true if the word is a palindrome, false otherwise. A palindrome is a word that is spelled the same forwards and backwards. x

def reverse(word):
  rev_word = ''

  i = len(word) - 1
  while i >= 0:
    rev_word += word[i]
    i -= 1

  return rev_word

def is_palindrome(word):
  return word == reverse(word)


print( is_palindrome("racecar") ) # => true
print( is_palindrome("kayak")   ) # => true
print( is_palindrome("bootcamp")) # => false