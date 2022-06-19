def findsortedposition(seq, target):
    low = 0
    high = len(seq)-1
    while low <= high:
        mid = (low + high)// 2
        if seq[mid] == target:
            print seq[mid]
            return mid
        elif target < seq[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None
