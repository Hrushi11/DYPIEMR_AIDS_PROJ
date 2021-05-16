def isPrime(n):
    c=0 
    for i in range(2,n):
        if n%i==0:
            c=c+1
    
    
    if c==0 and n!=1:
        return 1
    else:
        return 0
    
def sum(a,b):
    '''
    Adds to numbers
    input: a, b - two numbers
    output: returns sum
    '''
    c=a+b
    return c

def difference(a,b):
   '''
   subtracts two numbers
   input: a, b - two numbers
   output: returns difference
   '''
   c=a-b
   return c









