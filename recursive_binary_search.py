def recursive_binary(array, target):
    if len(array) == 0:
        return False
    else:
        mid_point = len(array)//2
    if array[mid_point] ==  target:
        return True
    elif array[mid_point] > target:
        return recursive_binary(array[:mid_point-1], target)
    else:
        return recursive_binary(array[mid_point+1:], target)


array = [1,2,3,4,5,6,7,8,9]
print(recursive_binary(array, 12))
