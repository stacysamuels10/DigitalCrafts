class BankAccount:
    def __init__ (self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
    def deposit (self, addMoney):
        self.balance = self.balance + addMoney
    def withdraw(self, addMoney):
        self.balance = self.balance - addMoney
    def transfer_funds (self, TransFunds, ToAccount, FromAccount):
        ToAccount.deposit(TransFunds)
        FromAccount.withdraw(TransFunds)
    def __str__(self):
        return f"""
        {self.balance}
        {self.account_number}
        """


addMoney = 0
check_account = BankAccount(80, "3333")
savings_account = BankAccount(60, "4444")

#stacyAccount.deposit(5)
#stacyAccount.withdraw(1)

savings_account.transfer_funds(10, savings_account, check_account)
print(check_account.balance)
print(savings_account.balance)