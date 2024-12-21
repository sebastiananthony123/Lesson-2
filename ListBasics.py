nums = [2 , 4 , 7 , 9, 9, 8 , 7 , 6 ,3]

print(nums[5])
print(nums[-2])

names = ['Kiran', 'John' , 'Dhriti' , 'Dhananjay']
print(names[3])

values = ['Alex' , 3 , 6.5 , True]
print(values)

print("--------------")
check = [nums , names]
print("COMBINED LIST")
print(check)

nums.insert(2,77)
print("INSERT")
print(nums)

names.append("Tarun")
print("APPEND")
print(names)

nums.extend([45,66,76,45,35])
print(nums)

nums.remove(8)
print(nums)

nums.pop(1)
print(nums)

nums.pop()
print(nums)

del names[3:]
print(names)

print("Smallest number :" , min(nums))
print("Greatest number :" , max(nums))
print("Sum :" , sum(nums))

nums.sort()
print(nums)
print(nums[4])

names.sort()
print(names)

nums.sort(reverse = True)
print(nums)

names.sort(reverse=True)
print(names)

name_copy = names.copy()
print(name_copy)
min_value = min(nums)
print("The minimum value is:", min_value)

join_list = names + nums
print(join_list)

index_name = names.index("Dhriti")
print(index_name)

print(nums.count(7))

print("----------")

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result = [a + b for a, b in zip(list1, list2)]

print(result)

numbers = [1, 2, 3, 4, 5, 6, 7]

squared_number = [x**2 for x in numbers]
print(squared_number)

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for a, b in zip(list1, list2[::-1]):
    print (a,b)
	