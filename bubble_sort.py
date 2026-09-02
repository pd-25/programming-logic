nums = [23, 4, 34, 2, 1, 212, 443]




def bubble_sort(nums: list) -> list:
    for i in range(len(nums) -1):
        swapped = False
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break

    return nums

print(bubble_sort(nums))