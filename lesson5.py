#from array import array


#a = array( 'i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#print(a.pop())
#print(a)

def is_power(a, b):
    names = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    if a == 1:
        return(1)
    elif a % b:
        return(0)
    else:
        return is_power(a // b, b)
def rain():
    n=int(input())
    a = [int(i) for i in input().split()]
    stepen=int(input())
    summma=0
    for i in range(n):
        summma=summma+(is_power(a[i], stepen))
    print(summma)