#Arithmetic operators
a = 10
b = 3
print(a + b) # Output: 13
print(a - b) # Output: 7
print(a * b) # Output: 30
print(a / b) # Output: 3.3333333333333335
print(a % b) # Output: 1
print(a ** b) # Output: 1000

#comparision operator
a = 10
b = 3
print(a > b) # Output: True
print(a < b) # Output: False
print(a == b) # Output: False
print(a != b) # Output: True
print(a >= b) # Output: True
print(a <= b) # Output: False

#Logical Operator
a = 10
b = 3
c = 5
print(a > b and b > c) # Output: False
print(a > b or b > c) # Output: True
print(not(a > b)) # Output: False

#assignment operator
a = 10
b = 3

a += b # same as a = a + b
print(a) # Output: 13

a -= b # same as a = a - b
print(a) # Output: 10

a *= b # same as a = a * b
print(a) # Output: 30

a /= b # same as a = a / b
print(a) # Output: 10.0

a %= b # same as a = a % b
print(a) # Output: 1.0

a **= b # same as a = a ** b
print(a) # Output: 1.0


#bitwise operator
a = 10 # binary 1010
b = 3 # binary 0011

print(a & b) # Output: 2 (binary 0010)
print(a | b) # Output: 11 (binary 1011)
print(a ^ b) # Output: 9 (binary 1001)
print(~a) # Output: -11
print(a << 2) # Output: 40 (binary 101000)
print(a >> 2) # Output: 2 (binary 0010)

