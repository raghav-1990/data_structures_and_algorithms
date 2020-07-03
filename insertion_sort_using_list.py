array = [5, 1, 6, 2, 4, 3]

def insertion_sort(a):
    for i in range(1, len(a)):
        currentValue = a[i]
        currentPosition = i
        while currentPosition > 0 and currentValue < a[currentPosition-1]:
            a[currentPosition] = a[currentPosition-1]
            currentPosition = currentPosition - 1
        a[currentPosition] = currentValue
    return a

print insertion_sort(array)
