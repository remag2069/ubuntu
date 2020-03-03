# n=int(input())

def f(n):
    print(n)
    if n<=1:
        return 1
    sum=0
    if n/2>=1:
        sum+=f(int(n/2))
    if n/3>=1:
        sum+=f(int(n/3))
    if n/4>=1:
        sum+=f(int(n/4))
    

print(f(50))