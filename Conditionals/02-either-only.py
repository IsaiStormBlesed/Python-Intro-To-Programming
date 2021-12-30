#Write a method either_only(number) that takes in a number and returns true if the number is divisible by either 3 or 5, but not both. The method should return false otherwise.

def either_only_v1(number):
  if number % 3 == 0 and number % 5 == 0:
    return False
  elif number % 3 == 0 or number % 5 == 0:
    return True 
  
  return False

def either_only(number):
  if not(number % 3 == 0 and number % 5 == 0) and (number % 3 == 0 or number % 5 == 0):
    return True
  
  return False

print( either_only(9) ) # => true
print( either_only(20)) # => true
print( either_only(7) ) # => false
print( either_only(15)) # => false
print( either_only(30)) # => false