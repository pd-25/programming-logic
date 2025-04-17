"""
 You are given an array, return all pairs that are the sums of given target
 
 1. loop through the array
 2. then check current element and it's each next element sums the target.
 
"""

theArray = [1,2,3,4,5,6,7,8,9]
target = 10
thePairs = []

# time complexity of this apporch is O(n^2)
# for currentElement in range(len(theArray)):
#     for nextElement in range(currentElement+1, len(theArray)):
#         if theArray[currentElement] + theArray[nextElement] == target:
#             print('pair of target sum is- ',theArray[currentElement], theArray[nextElement])
#             thePairs.append([theArray[currentElement], theArray[nextElement]])
# print('all pairs of target sum is- ',thePairs)

# time complexity of this apporch is O(n)
def pairs(theArray, target):
    seen = set()
    thedefPairs = []
    for singleEle in theArray:
        diff = target - singleEle
        if diff in seen:
            thedefPairs.append([singleEle, diff])
        seen.add(singleEle)
    # print(seen, thedefPairs)
    return thedefPairs
    

print(pairs(theArray, target))

    
    

