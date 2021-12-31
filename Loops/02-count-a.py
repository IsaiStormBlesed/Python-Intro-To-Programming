#Write a method count_a(word) that takes in a string word and returns the number of a's in the word. The method should count both lowercase (a) and uppercase (A)

def count_a(word):
  letters_a = 0

  i = 0
  while i < len(word):
    if word[i] == 'a' or word[i] == 'A':
      letters_a += 1
    i += 1

  return letters_a

print( count_a("application"))  # => 2
print( count_a("bike")       )  # => 0
print( count_a("Arthur")     )  # => 1
print( count_a("Aardvark")   )  # => 3