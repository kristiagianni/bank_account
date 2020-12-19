class BankAccount:
  interest_rate = float(0.01)
  accounts = []
  
  def __init__(self, balance=0):
    self.balance = balance
    __class__.accounts.append(self) 

  def deposit(self, deposit_amt):
    self.balance += deposit_amt

  def withdraw(self, withdraw_amt):
    self.balance -= withdraw_amt

  @classmethod
  def total_funds(cls):
    all_accts = 0
    for total in cls.accounts:
      all_accts += total.balance
    return all_accts

  @classmethod
  def add_interest(cls):
    for interest in cls.accounts:
     interest.balance += interest.balance * cls.interest_rate

def main():
  my_account = BankAccount()
  your_account = BankAccount()
  
  print(my_account.balance) #--> 0
  print(BankAccount.total_funds()) #--> 0
  
  my_account.deposit(200)
  your_account.deposit(1000)
  print(my_account.balance) #--> 200
  print(your_account.balance) #--> 1000
  print(BankAccount.total_funds()) #--> 1200
  
  BankAccount.add_interest()
  print(my_account.balance) #--> 202.0
  print(your_account.balance) #--> 1010.0
  print(BankAccount.total_funds()) #--> 1212.0
  
  my_account.withdraw(50)
  print(my_account.balance) #--> 152.0
  print(BankAccount.total_funds()) #--> 1162.0

main()
