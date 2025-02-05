def multiple_tuple(nums):
    temp=list(nums)
    product=1
    for x in temp:
        product*=x
    return product
nums = (4,3,2,2,-1,18)
print('Original Tuple: ')
print(nums)
print('product - multiplying all the numbers of the said tuple:',multiple_tuple(nums))

nums = (1,2,43,5,5,6,7,0,-21)
print('\n Original Tuple: ')
print(nums)
print('product - multiplying all the numbers of the said tuple:',multiple_tuple(nums))
