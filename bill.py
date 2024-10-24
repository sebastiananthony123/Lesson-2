units = int(input(" Please enter Number of Units consumed by you : "))

if(units<50):
    amount = units * 2.60
    surchrage = 25

elif(units<=100):
    amount = 130 + ((units - 50 ) * 3.25)
    surchrage = 35

elif(units<=200):
    amount = 130 + 162.50 +((units - 50 ) * 5.26)
    surchrage = 45

else:
    amount = 130 + 162.50 +((units - 200 ) * 8.45)
    surchrage = 75

total = amount + surchrage
print("\nElecticity Bill = %.2f"  %total)

