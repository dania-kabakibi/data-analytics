''' Lab 2 '''

def display_mailing_label(name, address, city, state, zip):
    print(f"{name}\n{address}\n{city} {state} {zip}")

def add_numbers(*args):
    total = sum(args)
    equation = " + ".join(map(str, args))
    print(f"{equation} = {total}")

def display_receipt(total_due, amount_paid):
    difference = amount_paid - total_due
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")
    if difference >= 0:
        print(f"Change Due: ${difference:.2f}")
    else:
        print(f"Remaining Balance: ${abs(difference):.2f}")


# --- Test Calls ---
print("--- Display two different addresses ---")
display_mailing_label("James Smith","8779 Windsor St","Fuquay Varina", "NC", "27526")
print()
display_mailing_label("Ronald Clark","131 Iroquois Street","Southgate", "MI", "48195")
print('-' * 40)

print("--- Add numbers ---")
add_numbers(6)
add_numbers(2, 7)
add_numbers(1, 3, 5, 7, 2)
print('-' * 40)

print("--- Display Receipts ---")
display_receipt(37.50, 40)
print()
display_receipt(45.82, 45.82)
print()
display_receipt(32.98, 30)
