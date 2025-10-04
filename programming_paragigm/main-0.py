# main-0.py
from bank_account import BankAccount

def main():
    # Initialize account (starting balance = 0)
    account = BankAccount()

    import sys
    if len(sys.argv) != 2:
        print("Usage: python main-0.py <operation>")
        print("Example: python main-0.py deposit:50")
        return

    operation = sys.argv[1]

    if ":" in operation:
        action, amount_str = operation.split(":", 1)
        try:
            amount = float(amount_str)
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
            return

        if action == "deposit":
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        elif action == "withdraw":
            if account.withdraw(amount):
                print(f"Withdraw: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid operation. Use 'deposit' or 'withdraw'.")
    elif operation == "display":
        account.display_balance()
    else:
        print("Invalid operation. Use 'deposit:<amount>', 'withdraw:<amount>', or 'display'.")

if __name__ == "__main__":
    main()