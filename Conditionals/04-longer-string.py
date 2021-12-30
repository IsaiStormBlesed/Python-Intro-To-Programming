#Write a method longer_string(str1, str2) that takes in two strings and returns the longer of the two strings. In the case of a tie, the method should return the first string.

def longer_string(str1, str2):
  str1_len = len(str1)
  str2_len = len(str2)
  if str1_len == str2_len or str1_len > str2_len:
    return str1
  else:
    return str2


print( longer_string("app", "academy")) # => "academy"
print( longer_string("summer", "fall")) # => "summer"
print( longer_string("hello", "world")) # => "hello"