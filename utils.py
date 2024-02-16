import math
def prime(n):
    ans=True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            ans=False
    return ans

def factorial(n):
    if n==1 or n==0: return 1
    else:
        return n*factorial(n-1)
