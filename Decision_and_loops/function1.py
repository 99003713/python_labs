import math

# Biggest of three numbers_____________________________


def greater(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z


# Check if given number is armstrong or not--------------------------------------------------

def armstrong(x):

    sum = 0
    dup1 = x

    r = 0
    l = int(math.log10(x))+1

    while x > 0:

        r = x % 10
        sum += r**l
        x = x//10

    if dup1 == sum:
        return 1

    else:
        return 0


# Reverse the number, sum of digits----------------------------------------
def revsum(x):
    sum = 0
    r = 0
    rev = 0
    while x > 0:
        r = x % 10
        sum = sum + r
        rev = rev*10 + r
        x = x//10

    print("Reverse value is : ", rev)
    print("sum of digit is : ", sum)


# GCD of two number------------------------------------------------------

def gcd(x, y):
    while(x != y):
        if x > y:
            x = x-y
        else:
            y = y-x
    return x


# LCM OF two number without GCD--------------------------------------------

def lcm(x, y):
    big = 0
    if(x > y):
        big = x
    else:
        big = y

    while(True):
        if(big % x == 0 and big % y == 0):
            lcm = big
            break
        big = big+1

    return lcm



# Checking type of a traingle---------------------------------------------------

def traingletype(x, y, z):
    if(x+y >= z or y+z >= x or z+x >= y):
        if(z == y == z):
            print("equilateral traingle")
        elif(x == y or y == z or z == x):
            print("isosceles traingle")
        elif((x*x == (z*z+y*y)**0.5) or (y*y == (x*x+z*z)**.5) or (z*z == (x*x+y*y)**.5)):
            print("right traingle")
        else:
            print("scalene traingle")
    else:
        print("NOT a valid traingle")

# finding roots-----------------------------------------------------------------


def root(a, b, c):

    d = b*b-4*a*c
    if(d > 0):
        r1 = (-b+d**.5)/2*a
        r2 = (-b-d**.5)/2*a
        print("Uniq roots are : ", r1, r2)
    elif(d == 0):
        r1 = r2 = (-b/2)*a
        print("both are same roots :", r1, r2)
    else:
        real = -b/2*a
        img = (-d)**.5/2*a
        print("Real and imaginary roots are :", real, img)


# quadrant of given points -------------------------------------------------------
def quadrant(x, y):
    if(x == 0 and y == 0):
        return 0
    elif(x > 0 and y > 0):
        return 1
    elif(x < 0 and y < 0):
        return 3
    elif(x > 0 and y < 0):
        return 4

# choice based calculation-----------------------------------------------------------


def calculator(x, y):

    print("for addition pls a Enter : 1")
    print("for subtraction pls a Enter : 2")
    print("for multiplication pls a Enter : 3")
    print("for division pls a Enter : 4")
    print("for mod pls a Enter : 5")
    print("for power pls a Enter : 6")
    print("for floor division pls a Enter : 7")

    choice = int(input("Enter your choice : "))

    if(choice == 1):
        return x+y
    elif(choice == 2):
        return x-y
    elif(choice == 3):
        return x*y
    elif(choice == 4):
        return x/y
    elif(choice == 5):
        return x % y
    elif(choice == 6):
        return x**y
    elif(choice == 7):
        return x//y


# Fibonacci series------------------------------------------------------------
    li = [0, 0, 1]
    # li.append(0)
    # li.append(1)

    for i in range(3, n):
        li.append(li[i-1]+li[i-2]+li[i-3])
        # n = n-1
    return li


# factorial of a number-------------------------------------------------------

def fact(n):
    facto = 1

    while(n > 0):
        facto = facto*n
        n = n-1

    return facto



# some of factor of a number---------------------------------------------------

def sumfactor(n):
    sum = 0
    i=1
    while(i < n):
        if(n%i == 0):
            
            sum = sum + i
        i = i+1
    return sum


# checking vowel.consonent-----------------------------------------------------------

def checkchar(n):
    if((n>='a' and n<='z') or (n>='A' and n<='Z')): 
        if(n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u' or n == 'A' or n == 'E' or n == 'I' or n == 'O' or n == 'U'):
            print("given character is a vowel")
        else:
            print("given character is a consonant") 
    else:
        print("please enter a valid character")             

#digital root of given number-------------------------------------------------------
def digital(x):
    sum = 0
    sum1 = 0
    while(x>0):
        r = x%10
        sum = sum + r
        x = x//10
    
    if(sum >= 10):
        digital(sum)

    else:
        print("digital root :: ",sum)


# List/count of prime numbers for given range----------------------------------------------
def range(x,y):
    i = 0
    count  = 0
    flag = 0
    j = 2
    while(x<=y):
        flag = 0
        j = 2
        while(j<x):
            if(x%j == 0):
                flag = 1
                break
            j = j+1
        if(flag == 0):
            print(x)
            count = count+1

        x = x+1
    print("total number of prime number : ",count)

# Sum of triangular numbers, n=4, 1 + (1+2) + (1+2+3) + (1+2+3+4) = 20----------------------------
def sumoftr(x):
    sum = 0
    i = 0
    j = 0
    for i in range(1, x+1):
        for j in range(1, i+1):
            sum = sum + j
    return sum


# Maximum number by deleting single digit in a 4 digit number----------------------------
#      5872  - 872,   9865 - 985

def maxafter(n):
    a = 0
    i = 1
    # t = 0
    while (n//i > 0):
        t=(n//(i*10))*i+(n%i)
        i = i*10
        if t>a:
            a = t
    return a  

# Generate super prime numbers----------------------------------------------------------
def superprime(n):
    count = 0
    i = 0
    li = []
    for i in range (2,n+1):
        flag = 0
        for j in range (2,i):
            if(i%j == 0):
                flag = 1
                break
       
        if(flag == 0):
            li.append(i)
            count = count+1        

    for i in range (2,count):
        flag = 0
        for j in range (2,i):
            if(i%j == 0):
                flag = 1
                break
       
        if(flag == 0):
            print(li[i])

# No.of combinations for n teams to play each other,  i.e. nCr------------------------------------

def comb(n):
    return(ft(n)/(ft(n-2)*ft(2)))

def ft(n):
    fact = 1
    i = 0
    for i in range(1,n+1):
        fact = fact*i
    return fact    



# Generate number triangles/pyramids, pascal triangle-----------------------------------------------
def pattern(n):
   
    # number triangle
    i = 0
    j = 0
    for i in range(n):
        for j in range(i):
            print(j,end='')
       
        print("")
   

      # number triangle
    i = 1
    j = 1
    k = 1
    for i in range (1,n+1):
        for k in range(1,n-i+1):
            print(" ",end='')
        for j in range(1,i+1):
            print(j,end='')
        for j in range(2,i+1):
            print(j,end='')    
       
        print("")    
