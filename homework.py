x = int(input("Enter a temp and dont type celsius symbol: "))

if x < 19:
    print(f"{x} It is not good to wear light clothes")

elif x > 19:
    print(f"{x}It is good to wear light clothes")

else:
    print(f"{x} it is okay...")