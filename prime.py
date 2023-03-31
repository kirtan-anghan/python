num = range(0,1000)

def prime_num(num):
    for i in range(2,num):
        if num % i  == 0:
          return False
    return True

prime = list(filter(prime_num , num))

print (prime)


