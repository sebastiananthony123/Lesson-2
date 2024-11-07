
for i in range(1,10):
    for j in range(1,i + 1):
        print("💰" , end = " ")
    print("\r")


for i in range(10,0,-1):
    for j in range(1,i + 1):
        print("💰", end = " ")
    print("\r")


for i in range(1,10):
    for j in range(1,i +1):
        print("💰", end = " ")
    print("\r")


for i in range(10,0,-1):
    for j in range(1,i + 1):
        print("💰", end = " ")
    print("\r")


for i in range(1,10):
    for j in range(1,i + 1):
        print("💰" , end = " ")
    print("\r")


for i in range(10,0,-1):
    for j in range(1,i + 1):
        print("💰", end = " ")
    print("\r")


for i in range(1,10):
    for j in range(1,i +1):
        print("💰", end = " ")
    print("\r")


for i in range(10,0,-1):
    for j in range(1,i + 1):
        print("💰", end = " ")
    print("\r")


print("\n\n------------Mulitplication table------------------\n\n")

for i in range(1,11):
    for j in range(1,11):
        print(i * j , end = " ")
    print("\r")


print("-------------")

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
         print(num, "is a prime number")
else:
    print(num, "is not a prime number")