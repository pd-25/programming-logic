nums = [23,23,23,4,34,34,2,1,212,34,443,23]

seen = set()
result = []
for num in nums:
    if num  not in seen:
        seen.add(num)
        result.append(num)


print(result)