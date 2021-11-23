#shell sort uses insertion sort
def shellsort(array):
    n = len(array)
    interval = n//2
    while interval >0:
        for i in range(interval ,n):
            current_position = i
            current_value = array[i]
            while current_position >= interval and current_value < array[current_position-interval]:
                array[current_position] = array[current_position-interval]
                current_position = current_position-interval
            array[current_position] = current_value
        interval //= 2
    return array
print(shellsort(array))
