
def printrev(n):
    if n > 0:
        print n
        printrev(n-1)

def printinc(n):
    if n > 0:
        printinc(n-1)
        print n

def factorial(n):
    if n >= 0:
        if n < 2:
            return 1
        else:
            return n * factorial(n-1)

def fibonacci(n):
    if n <= 0:
        print "incorrect"
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

# for i in range (10):
#     print fibonacci(i)

def hanoi(n, src, dest, temp):
    if n >= 1:
        hanoi(n-1, src, temp, dest)
        print "Move %d -> %d" % (src, dest)
        hanoi(n-1, temp, dest, src)

# hanoi(5, 1,3,2)

def expo(x, n):
    if n ==0:
        return 1
    result = expo(x*x, n//2)
    if n % 2 == 0:
        return result
    else:
        return x * result

print expo(3, 6)
