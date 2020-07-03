array = [5, 1, 6, 2, 4, 3]

def bubble(a):
    for i in range(len(a)):
        swapped = False
        j = 0
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
            j += 1
        if not swapped:
            break
    return a


print bubble(array)
