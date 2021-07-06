def selectionSort(array: list) -> list:
    length = len(array)

    for i in range(length):
        smallest = i

        for j in range(i + 1, length):
            if(array[smallest] > array[j]):
                smallest = j

        temp = array[i]
        array[i] = array[smallest]
        array[smallest] = temp

    return array


array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(selectionSort(array))
