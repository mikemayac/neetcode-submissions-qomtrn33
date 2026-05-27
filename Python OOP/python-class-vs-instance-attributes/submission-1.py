class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0
    
    def __init__(self, name: str, balance: int) -> None:
        self.__name = name
        self.__balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance
    
    @property
    def name(self) -> str:
        return self.__name

    @property
    def balance(self) -> int:
        return self.__balance

    def get_total_accounts() -> int:
        return BankAccount.total_accounts

    def get_total_balance() -> int:
        return BankAccount.total_balance

# TODO: Create two accounts
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format
print(f"{account1.name}'s balance: ${account1.balance}")
print(f"{account2.name}'s balance: ${account2.balance}")
print(f"Total Accounts: {BankAccount.get_total_accounts()}")
print(f"Total Balance: ${BankAccount.get_total_balance()}")
