# Given a sorted array of integers, write a function to search for a target value using binary 
# search. If the target is found, return its index, otherwise return -1.

def searchFromSortedArray(sortedArray, targetValue):
    firstElement = sortedArray[0]
    lastElement = sortedArray[len(sortedArray) -1]
    midElement = lastElement/2
    print(midElement)

numberList = [3,4,5,6,7,8,9,12,23,34]
searchFromSortedArray(numberList, 9)
    
    