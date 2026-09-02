data = [23,23,10,34,45,90,90,89,10,1,2,3,4,5,6,7,2]

data_dct = {} 
for single_d in data:
    data_dct[single_d] = data_dct.get(single_d, 0)+1

dup_list = [key for key, sing_dit in data_dct.items() if sing_dit > 1]

print(dup_list)


        

#Another approch
sen = set()
dup = set()

for num in data:
    if num in sen:
        dup.add(num)
    else:
        sen.add(num)

print(list(dup))