# Function to convert decimal number

# to binary using recursion

def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')

# decimal value

dec_val = int(input("Enter a number: "))


# Calling function

DecimalToBinary(dec_val)