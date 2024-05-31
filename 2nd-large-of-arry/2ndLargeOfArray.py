"""
 How would you find the second largest number in an array
 
 1. define two variable large and snd_large as 0
 2. then loop the array
 3. now check if large is smaller than current array element or not
 4. if smaller, 
"""

theArray = [82,43,23,112,4,42,23,1,2,44,42,9384,23,23,13,4,53]
large = 0
s_Large = 0
for singleEle in theArray:
    if large < singleEle:
        s_Large = large
        large = singleEle
        
print('2nd large is- ',s_Large)
print('large is- ',large)
    