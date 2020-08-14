def binarysearch(thevalues, target):
    low = 0
    high = len(thevalues) - 1
    while low <= high:
        mid = (low + high) // 2
        if thevalues[mid] == target:
            return True
        elif target < thevalues[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
