def bubbleSort(array: list) -> list:
    length = len(array) - 1

    for i in range(length):
        for j in range(length):
            if(array[j] > array[j + 1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j + 1] = temp

    return array


array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(bubbleSort(array))
