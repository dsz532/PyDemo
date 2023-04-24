import sys
def fibonacci(n):
    a,b,counter=0,1,0
    while counter<=n:
        yield a
        a,b=b,a+b
        counter+=1
    else:
        return
f=fibonacci(10)
while True:
    try:
        print(next(f),end=' ')
    except StopIteration:
        sys.exit()

