def check_age():
    try:

        age = int(input("Enter your age: "))

        if age < 0:
            raise ValueError("Your age can't be negative!")
        
        if age % 2 == 0:
            print(f"Your age is {age}, which is even.")
        else:
            print(f"Your age is {age}, which is odd.")
        
    except ValueError as e:
        print(f"Error: e")
    except Exception as e:
        print(f"An unexpected error has occured: {e}")


check_age()




print("------------Example 2-------------")

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Can't divide by 0!")
    else:
        print(f"The result is: {result}")

divide_numbers(10, 2)
divide_numbers(10, 0)


print("------------Example 3-------------")


def get_integer():
    while True:
        try:
            num = int(input("Enter an interger: "))
            return num
        except ValueError:
            print("That's not an integer. Try again.")

value = get_integer()
print(f"You entered: {value}")

print("------------Example 5------------")

def process_data(data):
    try:
        result = 100 / data
        print(f"Result: {result}")
    except (ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")

process_data(10)
process_data(0)
process_data("a")


print("--------Example 5----------")



def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Your age is: {age}")

try:
    check_age(25)
    check_age(-5)
except ValueError as e:
    print(f"Error: {e}")

print("-----------Example 6------------")



def divide_with_finally(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Can't divide by 0!")
    finally:
        print("Execution completed.")

divide_with_finally(10, 2)
divide_with_finally(10, 0)

print("---------Example 7-----------")
def safe_input():
    try:
        number = int(input("Enter a number: "))
        print(f"You entered: {number}")
    except ValueError:
        print("Error: That wasn't a valid number:")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")

safe_input()