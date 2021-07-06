import requests
import sys

sys.setrecursionlimit(5000)


def swap(array: list, i: int, j: int):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def getPartition(array: list, left: int, right: int) -> int:
    pivotElement = array[right]
    partitionIdx = left

    for j in range(left, right):
        if (array[j] <= pivotElement):
            swap(array, partitionIdx, j)
            partitionIdx += 1

    swap(array, partitionIdx, right)

    return partitionIdx


def quickSort(array: list, left: int, right: int) -> list:
    if(left < right):
        partitionIndex = getPartition(array, left, right)

        quickSort(array, left, partitionIndex - 1)
        quickSort(array, partitionIndex + 1, right)

    return array


array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# url = 'https://leetcode-testcases.netlify.app/518032060/data.json'

# response = requests.get(url)

# array = response.json()

print(quickSort(array, 0, len(array) - 1))
