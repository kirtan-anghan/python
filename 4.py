#add two number by function
def add(x, y):
    return x + y

print( add(5,2))

#recursion function for power of numbers 

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)
print( power(5,2))
