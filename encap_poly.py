class MaxLimitExceededError(Exception):
    pass

class Bank:
    def __init__(self, bank_Name, max_transaction, max_amount):
        self.__bank_Name = bank_Name
        self.__max_transaction = max_transaction
        self.__max_amount = max_amount

    def get_bank_name(self):
        return self.__bank_Name
    def get_max_transaction(self):
        return self.__max_transaction
    def get_max_amount(self):
        return self.__max_amount
    def update_limits(self,amount):
        self.__max_transaction -= 1
        self.__max_amount -= amount

    def withdraw(self, amount):
        pass

class HDFC(Bank):
    def __init__(self):
        super().__init__("HDFC", 3, 20000)
    def withdraw(self, amount):
        if amount > self.get_max_amount():
            raise MaxLimitExceededError("Withdrawal amount exceeds the maximum limit.")
        if self.get_max_transaction() <= 0:
            raise MaxLimitExceededError("Maximum number of transactions exceeded.")
        self.update_limits(amount)
        print("withdrawal successful.")
        print("Bank Name:", self.get_bank_name())
        print("Amount Withdrawn:", amount)
        print("Remaining Amount Limit:", self.get_max_amount())
        print("Remaining Transaction Limit:", self.get_max_transaction())

class AXISBank(Bank):
    def __init__(self):
        super().__init__("AXIS Bank", 5, 30000)
    def withdraw(self, amount):
        if amount > self.get_max_amount():
            raise MaxLimitExceededError("Withdrawal amount exceeds the maximum limit.")
        if self.get_max_transaction() <= 0:
            raise MaxLimitExceededError("Maximum number of transactions exceeded.")
        self.update_limits(amount)
        print("withdrawal successful.")
        print("Bank Name:", self.get_bank_name())
        print("Amount Withdrawn:", amount)
        print("Remaining Amount Limit:", self.get_max_amount())
        print("Remaining Transaction Limit:", self.get_max_transaction())

class ATM:

    def inputAmount(self):

        print("Select your bank")
        print("1. HDFC")
        print("2. AXIS")

        while True:

            choice = input("Select your bank (1 or 2): ")

            if choice == "1":
                bank = HDFC()
                break

            elif choice == "2":
                bank = AXISBank()
                break

            else:
                print("Invalid choice. Please try again.")

        while True:

            try:
                amount = float(input("Enter the amount to withdraw: "))

                if amount <= 0:
                    print("Amount must be greater than zero. Please try again.")
                    continue
                bank.withdraw(amount)

            except MaxLimitExceededError as e:
                print("\nError: ", e)
                print("transaction terminated.")
                break

            except ValueError:
                print("Invalid input. Please enter a valid amount.")
                continue
            next_transaction = input(
                 "Do you want to perform another transaction? (yes/no): ").strip().lower()

            if next_transaction == "yes":
                 continue

            elif next_transaction == "no":
                 print("Thank you for using the ATM.")
                 break

            else:
             print("Invalid input. Please enter 'yes' or 'no'.")
             break
            
atm = ATM()
atm.inputAmount()

            
            
      