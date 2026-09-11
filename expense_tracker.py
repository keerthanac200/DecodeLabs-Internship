def expense_tracker():
    # Initialization (State preservation) - Initialized outside the loop
    total = 0.0

    print("=== DecodeLabs Expense Tracker ===")
    print("Enter expense amounts. Type 'quit' or 'exit' to stop.\n")

    # Continuous Audit Loop
    while True:
        user_input = input("Enter expense amount: ").strip()

        # Sentinel Value / Emergency Stop Check
        if user_input.lower() in ["quit", "exit"]:
            break

        # Defensive Coding / Digital Poka-Yoke (Error Handling)
        try:
            expense = float(user_input)

            if expense < 0:
                print("Error: Expense cannot be negative. Please enter a valid number.\n")
                continue

            # Accumulator Pattern: total = total + new_expense
            total += expense
            print(f"Added: ${expense:.2f} | Current Total: ${total:.2f}\n")

        except ValueError:
            print("Invalid Data: Please enter a valid numerical amount or 'quit'.\n")

    # Final Output Display
    print("=" * 35)
    print(f"FINAL TOTAL SPENT: ${total:.2f}")
    print("=" * 35)


if __name__ == "__main__":
    expense_tracker()