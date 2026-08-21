class AmountError(Exception):
    """Raised when the account amount does not meet the minimum requirement."""
    pass

class BankInfo:
    """Stores basic information of the bank customer."""
    def __init__(self, first_name, last_name, gender, address):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__address = address
    def get_name(self):
        """Return the customer's full name."""
        return self.__first_name + " " + self.__last_name
    def get_address(self):
        """Return the customer's address."""
        return self.__address

class BankAccount:
    """Stores bank account information."""
    def __init__(self, account_number, amount, bank_info):
        self.__account_number = account_number
        self.__amount = amount
        self.__bank_info = bank_info
    def get_amount(self):
        """Return the account amount."""
        return self.__amount
    def get_account_number(self):
        """Return the account number."""
        return self.__account_number
    def get_bank_info(self):
        """Return the BankInfo object."""
        return self.__bank_info

class Saving(BankAccount):
    """Represents a savings bank account."""
    MIN_AMOUNT = 10000
    RATE = 6
    def validate_amount(self):
        """Validate the minimum amount required for a savings account."""
        if self.get_amount() < self.MIN_AMOUNT:
            raise AmountError("Minimum amount for Saving Account is Rs.10000.")
        return True

    def calculate_interest(self, months):
        """Calculate simple interest for the given number of months."""
        return ( self.get_amount() * self.RATE * months) / (12 * 100)

class Current(BankAccount):
    """Represents a current bank account."""
    MIN_AMOUNT = 5000
    def validate_amount(self):
        """Validate the minimum amount required for a current account."""

        if self.get_amount() < self.MIN_AMOUNT:
            raise AmountError("Minimum amount for Current Account is Rs.5000.")
        return True
    def calculate_interest(self, months):
        """Current account does not provide interest."""
        return 0

def main():
    """Run the bank account application."""

    print("Bank Account System")
    print("\nEnter Bank Information")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    gender = input("Enter gender: ")
    address = input("Enter address: ")

    bank_info = BankInfo(first_name, last_name, gender, address)
    print("\nEnter Bank Account Information")
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount: "))

    bank_account = BankAccount(account_number, amount, bank_info)

    print("\nSelect Account Type")
    print("1. Saving")
    print("2. Current")

    choice = input("Enter your choice: ")

    if choice == "1":
        account = Saving(bank_account.get_account_number(), bank_account.get_amount(), bank_account.get_bank_info())

    elif choice == "2":
        account = Current( bank_account.get_account_number(), bank_account.get_amount(), bank_account.get_bank_info() )

    else:
        print("Invalid account type.")
        return

    for attempt in range(3):
        try:
            account.validate_amount()
            print("Amount is valid.")
            break

        except AmountError as error:
            print("Amount Error:", error)

            if attempt == 2:
                print("You have used all 3 chances.")
                return

            print("Please try again.")
            amount = float(input("Enter amount again: "))

            if choice == "1":
                account = Saving(bank_account.get_account_number(), amount, bank_account.get_bank_info())
            else:
                account = Current(bank_account.get_account_number(), amount, bank_account.get_bank_info())

    months = int(input("\nEnter number of months: "))
    interest = account.calculate_interest(months)

    print("\nAccount Details:")
    print("Name:", account.get_bank_info().get_name())
    print("Address:", account.get_bank_info().get_address())
    print("Account Number:", account.get_account_number())
    print("Amount:", account.get_amount())

    if choice == "1":
        print("Account Type: Saving")
        print("Interest Rate:", Saving.RATE, "%")
        print("Interest:", interest)
    else:
        print("Account Type: Current")
        print("Interest Rate: No Interest")
        print("Interest:", interest)
    print("Total Amount:", account.get_amount() + interest)

if __name__ == "__main__":
    main()