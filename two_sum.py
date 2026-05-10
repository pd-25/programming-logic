def two_sum(nums, target):
    for i,v in enumerate(nums):
        diff = target- v
        if diff in nums:
            dif_index=nums.index(diff)
            if i != dif_index:
                return [i, dif_index]
    
    
        
    