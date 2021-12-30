num = 40
num + 5
print("--1--")
print(num)                  #40

num += 2
print("--2--")
print(num)                  #42

is_Even = num % 2 == 0
print("--3--")
print(is_Even)              #True

is_Negative = num < 0
print("--4--")
print(is_Negative)          #False

print("--5--")
print(is_Negative or is_Even) #True

print("--6--")
print(is_Even and is_Negative) #False

print("--7--")
print(is_Even and not is_Negative) #True

