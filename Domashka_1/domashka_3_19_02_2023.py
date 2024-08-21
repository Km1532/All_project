a = int(input())
b = int(input())
c = int(input())
d = b*b-4*a*c
if d < 0:
    print("No roots")
else:
    x1 = int((-b+d**0.5)/(2*a))
    x2 = int((-b-d**0.5)/(2*a))
if x1==x2:
    print("One root:" ,x1)
else:
    print("Two roots:" ,x2,x1)

