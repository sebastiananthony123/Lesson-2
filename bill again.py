total_bill = float(input("Enter the total bill amount:  $"))
amount_paid = float(input("Enter the amount paid by the customer: $"))

if amount_paid >= total_bill:
    print("No due amount. The customer has overpaid or paid the exact amount.")
else:
    due_amount = total_bill - amount_paid
    print(f"The due amount the customer needs to pay is: ${due_amount:.2f}")
    