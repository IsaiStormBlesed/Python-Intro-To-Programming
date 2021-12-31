#Write a method, count_vowels(word), that takes in a string word and returns the number of vowels in the word. Vowels are the letters a, e, i, o, u.

def count_vowels(word):
  vowels_count = 0
  vowels = 'aeiou'

  i = 0
  while i < len(word):
    if word[i] in vowels: #Using conditionals 
      vowels_count += 1
    i += 1

  return vowels_count

print( count_vowels("bootcamp"))  # => 3
print( count_vowels("apple")   )  # => 2
print( count_vowels("pizza")   )  # => 2