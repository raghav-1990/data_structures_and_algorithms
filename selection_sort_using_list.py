array = [5, 1, 6, 2, 4, 3]

def select_sort(a):
    for i in range(len(a)):
        mini = i
        for j in range(i+1, len(a)):
            if a[mini] > a[j]:
                mini = j
        a[i], a[mini] = a[mini], a[i]
    return a

print select_sort(array)
