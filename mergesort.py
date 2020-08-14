def mergesort(seq1, seq2):
    newlist = list()
    seq1 = bubblesort(seq1)
    seq2 = insertionSort(seq2)
    a = 0
    b = 0
    while a < len(seq1) and b < len(seq2):
        if seq1[a] < seq2[b]:
            newlist.append(seq1[a])
            a += 1
        else:
            newlist.append(seq2[b])
            b += 1
    while a < len(seq1):
        newlist.append(seq1[a])
        a += 1
    while b < len(seq2):
        newlist.append(seq2[b])
        b += 1
    return newlist
a= [5,7,2]
b = [9, 4, 0, 11]
# print mergesort(a,b)
