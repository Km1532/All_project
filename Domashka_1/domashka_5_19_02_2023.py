a = int(input())
b = int(input())
c = int(input())
if ((b>=a) and (b<=c)) or ((b>=c) and (b<=a)):
    s=a+c
if ((c>=a) and (c<=b)) or ((c>=b) and (c<=a)):
    s=a+b
if ((a>=b) and (a<=c) or (a>=c) and (a<=b)):
    s=b+c
print(s)