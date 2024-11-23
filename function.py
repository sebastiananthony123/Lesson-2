

def add():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))    
    sum = x + y
    print(f"{x} + {y} = {sum}")
   



def sub():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))    
    ans = x - y
    print(f"{x} - {y} = {ans}")



def multiply():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))    
    ans = x + y
    print(f"{x} * {y} = {ans}")
   


def div():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))    
    ans = x / y
    print(f"{x} / {y} = {ans}")


print("What operation do you want to preform? ")
print("1.Addition")
print("2.Subraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("choose from {1-4} : "))
if choice == 1:
    add()

elif choice == 2:
    sub()

elif choice == 3:
    multiply()

elif choice == 4:
    div()

else:
    print("Invalid input")
