#Write a method word_check(word) that takes in a word and returns a string. The method should return the string "long" if the word is longer than 6 characters, "short" if it is less than 6 characters, and "medium" if it is exactly 6 characters long.

def word_check(word):
  if len(word) > 6:
    return 'long'
  elif len(word) < 6:
    return 'short'
  else:
    return 'medium'

print( word_check("contraption")) # => "long"
print( word_check("fruit")      ) # => "short"
print( word_check("puzzle")     ) # => "medium"