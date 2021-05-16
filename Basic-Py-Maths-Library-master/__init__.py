def isPrime(n):
    c=0 
    for i in range(2,n):
        if n%i==0:
            c=c+1
    
    
    if c==0 and n!=1:
        return 1
    else:
        return 0







