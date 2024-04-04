# 37. Bank Account

class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
  
  def deposit(self, amount):
    self.balance += amount
    return self.balance
  
  def withdraw(self, amount):
    self.balance -= amount
    return amount
  
  def display_balance(self):
    print(f'${self.balance}')

bank_account = BankAccount('Anna', 'Hills', 7463783, 'Savings account', 7261, 100.0)
bank_account.deposit(96)
bank_account.withdraw(25)
bank_account.display_balance()
