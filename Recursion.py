#factorial(7)=7*6*5*4*3*2*1
#factorial(6)=6*5*4*3*2*1
#factorial(5)=5*4*3*2*1
#factorial(4)=4*3*2*1
#factorial(0)=1

#factorial(n)=n*(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(4))
print(factorial(3))

#fibonacci Sequence
#f(0)=0
#f(1)=1
#f(2)=f(1)+f(0)
#f(n)=f(n-1)+f(n-2)

def fiboncci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fiboncci(n-1)+fiboncci(n-2)
print(fiboncci(6))
