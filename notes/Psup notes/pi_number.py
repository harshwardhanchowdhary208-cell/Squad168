a = 22/7
b = str(a)
c = int(input())
d = str(c)
b = b[2::1]
i=0
found = False
while i < len(b):
    if b[i:i+9] == d:
        print("Your number is found after {i} iterations")
        found = True
        break
    else:
        i += 1
if not found:
    print("Your number doesn't lie in this range of pi")