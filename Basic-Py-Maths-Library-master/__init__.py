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

def Fibonacci_Series(n):
    # base case
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (Fibonacci_Series(n-2) + Fibonacci_Series(n-1))

###############################

def MultiplyTwoNumbers(a,b):
    """
    multiplying two numbers
    input: a,b - two numbers
    output: returns multiplication
    """
    c = a*b
    return c

###############################

def MultiplyList(myList):
    """
    multiplying the numbers in list
    input: list
    output: returns the multiplication
            of numbers in given list
    """
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

################################

def ConvertToDegree(radian):
    """
    Converts radian to degree
    input: angle in radian
    output: angle in degree
    """

    radian = float(radian)
    pi = 22/7
    degree = float(radian * (180 / pi))
    return degree

################################

def ConvertToRadian(degree):
    """
        Converts degree to radian
        input: angle in degree
        output: angle in radian
        """
    degree = float(degree)
    pi = 22 / 7
    radian = float(degree * (pi / 180))
    return radian
  
################################

def exponent(base, index):
    '''
    finds the exponent 
    input:two numbers -base and index 
    ouptut- base raised to the index
    '''
    if index == 0:
        return 1
    while index > 1:
        x = base**index
        return x

################################

def Perimeter(a,b,c):
    '''
    Input: a = length of first side
           b = length of second side
           c = length of third side   
    Output - (a+b+c)
    '''
    return (a+b+c)

################################

def areaofcircle(r):
    """
    calculates area of a circle 
    input:radius of circle
    output:area of circle
    """
    PI = 3.14159265358
    area = PI*(r**2)
    return area

###############################

def circumferenceofcircle(r):
    """
    calculates circumference of circle
    input:radius of circle
    output:circumference of circle
    """
    PI = 3.14159265358
    cmf = PI*2*r
    return cmf

###############################

def factorial(n):
    
    '''
    calculates factorial
    input: non negative integer
    output: factorial of input
    '''
    
    if n<0:
        return 'Not defined for negative number'
    if n==0:
        return 1
    else:
        x= n*factorial(n-1)
        return x
    
###############################    

def fact_loop(num):
    '''
    input : num
    output : factorial
    '''
    if num < 0:
        return 0
    if num == 0:
        return 1

    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    print(factorial)
    
################################

def volume_cyl(r, h):
    return (3.14 * (r**2) * h)

################################

    








