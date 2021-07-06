def insertionSort(array: list) -> list:
    length = len(array)

    for i in range(length):
        if(array[i] < array[0]):
            array.insert(0, array.pop(i))
        else:
            for j in range(1, i):
                if(array[i] >= array[j-1] and array[i] < array[j]):
                    array.insert(j, array.pop(i))

    return array


array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(insertionSort(array))
