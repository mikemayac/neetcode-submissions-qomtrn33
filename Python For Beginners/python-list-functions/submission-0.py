from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    sum_list = 0
    for num in nums:
        sum_list+= num
    return sum_list

def get_min(nums: List[int]) -> int:
    min_list = nums[0]
    for num in nums:
        if min_list <= num:
            continue
        else: 
            min_list = num
    return min_list

def get_max(nums: List[int]) -> int:
    max_list = nums[0]
    for num in nums:
        if max_list >= num:
            continue
        else:
            max_list = num
    return max_list

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
