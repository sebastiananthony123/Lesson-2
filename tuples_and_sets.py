tup = (35,34,87,47,48,14,70)

print(tup[2])
print (tup[::-1])


reversed_subset = tup[0.6[::-1]]

print(reversed_subset)


even_index_elements = tup[0:6][::-1]

print(reversed_subset)


even_index_elements = tup[::2]

print(even_index_elements)

print("-------------------")
for num in tup:
    if num % 2 == 0:
        print(num)

print("------------")
fruits = ("apple", "banana", "grapefuit", "orange", "kiwi", "lemon", "mango")
print(fruits)
print(fruits[-3])
print(fruits[2:5])
print(len(fruits))

print("---------------")

for i in fruits:
    print(i)

del tup

def is_palindrome(tup):

    return tup == tup[::-1]

my_tuple = (1, 2, 3, 2, 1)  
another_tuple = (1, 2, 3, 4)

if is_palindrome(my_tuple):
    print(f"{my_tuple} is a palindrome.")
else:
    print(f"{my_tuple} is a not palindrome.")

if is_palindrome(another_tuple):
    print(f"{another_tuple} is a palindrome.")
    
else:
    print(f"{another_tuple} is not a palindrome.")

print("-----------")
def calculate_product(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

my_tuple = (2, 3, 4 ,5)
result = calculate_product(my_tuple)

print(f"The product of all number sin the tuple {my_tuple} is: {result}")