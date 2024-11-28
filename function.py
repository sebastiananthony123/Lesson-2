

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
    ans = x * y
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

print("------------------")

def area_calculator():
    print("What area do you want to calculate the area of?")
    print("1.Triangle")
    print("2.Square")
    print("3.Rectangle")
    print("4.Circle")

choice = int(input("Choose from 1-4: "))
if choice == 1:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("Area of the triangle : " , area)

elif choice == 2:
    size = float(input("Enter the size of the square: "))
    area = size * size
    print("Area of the Square : " , area)

elif choice == 3:
    length = float(input("Enter the base of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print("Area of the rectangle : " , area)

elif choice == 4:
    radius = float(input("Enter the radius of the circle: "))
    pi = 3.14
    area = pi * radius * radius
    print("Area of the circle : " , area)

else:
    print("Invalid Input....")

area_calculator()