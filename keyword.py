for i in range(21):
    if i % 5 == 0:
        continue
    print(i)

print("-------")

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break

    else:
        print(num, "is a prime number")
        
else:
    print(num, "invalid input") # type: ignore
print("-------------")
for i in range(1,21,1):
    if i % 3 == 0 and i % 5 ==0:
       print("fizz buzz")

    elif i % 3 == 0:
        print("fizz")       
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
print("***********")

number = int(input("Enter a number: "))
product = 1
for i in range(1,number + 1):
    product = product * i

print(f"The factorial of {number} is {product}")