array = ['433366789','433366790','433366791','433366792','433366793','433366793','433366793','433366793','433366793','433366794','433366794']

def duplicate_cutter(some_array):
    range_of_array = range(len(array))
    array2 = []
    for i in range_of_array:
        if i == range_of_array[-1]:
            if some_array[range_of_array[-1]] == some_array[range_of_array[-2]]:
                array2.append(some_array[i])
            else:
                array2.append(some_array[range_of_array[-1]])
        else:
            if some_array[i] != some_array[i+1]:
                array2.append(some_array[i])

    return array2

print(duplicate_cutter(array))