i = 1
while (i <= 10):
    print(i)
    i += 1
print("*********")

sum= 0
i= 1
while i <= 10:
  sum =sum+i
  i = i+1

print("\nSum =", sum)

print("----------")

n =int(input("Enter a number: "))

product= 1
i = 1
while i <= n:
  product = product * i
  i = i+1

print("\nproduct =", product)

print('----------')

number =int(input("Enter a number: "))

digits = str(number)
num_digits = len(digits)

armstrong_sum = 0
for digit in digits:
    armstrong_sum += int(digit) ** num_digits

if armstrong_sum == number:
    print(f"{number} is an armstrong number.")
else:
    print(f"{number} is an armstrong number. ")