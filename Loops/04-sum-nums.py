#Write a method sum_nums(max) that takes in a number max and returns the sum of all numbers from 1 up to and including max.

def sum_nums(max):
  sum = 0

  i = 1
  while i <= max:
    sum += i
    i += 1

  return sum

print( sum_nums(4)) # => 10, because 1 + 2 + 3 + 4 = 10
print( sum_nums(5)) # => 15