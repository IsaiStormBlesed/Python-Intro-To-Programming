#Write a method reverse(word) that takes in a string word and returns the word with its letters in reverse order.

def reverse(word):
  rev_word = ''

  i = len(word) - 1
  while i >= 0:
    rev_word += word[i]
    i -= 1

  return rev_word

print( reverse("cat")        )  # => "tac"
print( reverse("programming"))  # => "gnimmargorp"
print( reverse("bootcamp")   )  # => "pmactoob"