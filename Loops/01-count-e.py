#Write a method count_e(word) that takes in a string word and returns the number of e's in the word

def count_e(word):
  letters_e = 0

  i = 0
  while i < len(word):
    if word[i] == 'e':
      letters_e += 1
    i += 1

  return letters_e

print( count_e("movie")) # => 1
print( count_e("excellent")) # => 3