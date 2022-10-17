a = 1

while a< 5:
    b = 0
    while b < a:
        print("*",end=' ')
        b = b+1

    print()
    a = a+1

for a in range(1,6):
    for b in range(1,6):
        c = a*b
        print(c, end=" ")
    print()
