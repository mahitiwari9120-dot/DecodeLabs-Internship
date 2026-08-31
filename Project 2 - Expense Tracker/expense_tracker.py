# Expense Tracker Project
print("===== EXPENSE TRACKER =====")
print("Type 'done' when you have finished entering expenses.")
total = 0

while True:
    choice = input("Enter expense or type 'done' to finish: ")

    if choice.lower() == "done":
        break

    expense = float(choice)
    total = total + expense
    print("Total Spent: ₹", total)
