def isPrime(n):
    '''
    Checks for a prime number.<br>
    Input - `n`, any integer <br>
    Output - boolean value
    '''
    c=0 
    for i in range(2,n):
        if n%i==0:
            c=c+1
    
    
    if c==0 and n!=1:
        return 1
    else:
        return 0

###############################

def sum(a,b):
    '''
    Adds to numbers
    input: a, b - two numbers
    output: returns sum
    '''
    c=a+b
    return c

###############################

def difference(a,b):
   '''
   subtracts two numbers
   input: a, b - two numbers
   output: returns difference
   '''
   c=a-b
   return c

###############################

def fact_loop(num):
    if num < 0:
        return 0
    if num == 0:
        return 1

    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    print(factorial)
    
################################












