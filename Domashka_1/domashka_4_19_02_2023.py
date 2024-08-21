a = int(input())
b = int(input())
c = int(input())
if ((b>a) and (b<c)) or ((b>c) and (b<a)):
    s=b
if ((c>a) and (c<b)) or ((c>b) and (c<a)):
    s=c
if ((a>b) and (a<c) or (a>c) and (a<b)):
    s=a
print(s)