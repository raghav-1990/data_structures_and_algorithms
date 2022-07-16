def recursive_binary(array, target):
    if len(array) == 0:
        return False
    else:
        mid_point = len(array)//2
    if array[mid_point] ==  target:
        return True
    elif array[mid_point] > target:
        return recursive_binary(array[:mid_point], target)
    else:
        return recursive_binary(array[mid_point+1:], target)

#another attempt
def rec_binary_search(seq, target):
    if len(seq) == 0:
        return False
    else:
        mid = len(seq) //2
        if seq[mid] == target:
            return True
        elif seq[mid] > target:
            return rec_binary_search(seq[:mid], target)
        else:
            return rec_binary_search(seq[mid+1:], target)

array = [1,2,3,4,5,6,7,8,9]
print(recursive_binary(array, 12))
