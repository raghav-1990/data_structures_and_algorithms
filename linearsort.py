def linearsort(thevalues, target):
    n = len(thevalues)
    for i in range(n):
        if thevalues[i] == target:
            return True
    return False

def sortedlinearsort(thevalues, target):
    n = len(thevalues)
    for i in range(n):
        if thevalues[i] == target:
            return True
        elif thevalues[i] > target:
            return False
    return False

def findsmallest(thevalues):
    n = len(thevalues)
    smallest = thevalues[0]
    for i in range(n):
        if thevalues[i] < smallest:
            smallest = thevalues[i]
    return smallest
