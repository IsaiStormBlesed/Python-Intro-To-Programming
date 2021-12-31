#Write a method factorial(num) that takes in a number num and returns the product of all numbers from 1 up to and including num.

def factorial(num):
  product = 1

  i = 1
  while i <= num:
    product *= i
    i += 1

  return product
print( factorial(3)) # => 6, because 1 * 2 * 3 = 6
print( factorial(5)) # => 120, because 1 * 2 * 3 * 4 * 5 = 120