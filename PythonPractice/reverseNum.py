

number=54656

revnum=0

while number >0:
    dig=number%10
    revnum=revnum*10+dig
    number=number//10

print(revnum)