import math


def mergeSort(array: list) -> list:
    length = len(array)

    if length == 1:
        return array

    midPoint = math.floor(length / 2)

    left = array[0:midPoint]
    right = array[midPoint:length]

    return merge(
        mergeSort(left),
        mergeSort(right),
    )


def merge(left: list, right: list):
    merged = []

    leftIndex = 0
    rightIndex = 0

    while(leftIndex < len(left) and rightIndex < len(right)):
        if(left[leftIndex] < right[rightIndex]):
            merged.append(left[leftIndex])
            leftIndex += 1
        else:
            merged.append(right[rightIndex])
            rightIndex += 1

    return merged + left[leftIndex:len(left)] + right[rightIndex:len(right)]


array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(mergeSort(array))
