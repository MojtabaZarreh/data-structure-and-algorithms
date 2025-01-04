#dictionaries
# book = {}
# book["apple"] = 0.67 
# book["milk"] = 1.49 
# book["avocado"] = 1.49
# # print(book)


# print(book["apple"])


# voted = {}
# def checl_voter(name):
#     if name in voted:
#         print("kick them out!")
#     else:
#         voted[name]=True
#         print("let them vote !")
        
# checl_voter('Ali')
# checl_voter('Reza')
# checl_voter('Hasan')
# checl_voter('Reza') #kick them out!

# nums = [3,2,3]
# my_nums = {}
# for i in range(len(nums)):
#     my_nums[i] = nums[i]
# print(my_nums)

nums = [2,7,11,15]
target = 9
my_nums = {}
for i in range(len(nums)):
    tar = target - nums[i]
    print(tar)
    if tar in my_nums:
        print([my_nums[tar], i])
        break
    my_nums[i] = nums[i]
    print(my_nums)