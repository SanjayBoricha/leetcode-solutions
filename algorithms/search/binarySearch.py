import math


def binarySearch(array: list, target: int) -> int:
    left = 0
    right = len(array) - 1

    while(left <= right):
        mid = math.floor((left + right) / 2)

        if(array[mid] == target):
            return mid
        elif(array[mid] < target):
            left = mid + 1
        else:
            right = mid - 1

    return -1


array = []

for i in range(100000):
    array.append(i + 1)


print(binarySearch(array, 99))
