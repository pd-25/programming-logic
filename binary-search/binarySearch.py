"""How would you implement Binary Search?
1. get the arr length and hulf it.
2. then if first arr last value is > targetVal, then arr is first arr else arr is 2nd arr
3. then repeate this thing
"""
def binarySearch(arr, targetValue):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == targetValue:
            return mid
        elif arr[mid] < targetValue:
            low = mid + 1
        else:
            high = mid - 1
    return -1
    

theArr = [1,2,3,4,5,6,7,8,9,11]
targetVal = 7
print(f'The {targetVal} is present in the array index of {binarySearch(theArr, targetVal)}')