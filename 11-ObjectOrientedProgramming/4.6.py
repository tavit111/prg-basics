class BankAccount:

  def __init__(self, account_no):
    self.account_no = account_no.replace(" ", "") #usuwa spacje za pomocą replace(" ", ""), aby łatwo go później formatować)
    self.balance = 0.0

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount

  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
    else:
      print("Insufficient funds on the account")

  def display_info(self):
    formatted_no = (
        f"{self.account_no[:2]} {self.account_no[2:6]} {self.account_no[6:10]} "
        f"{self.account_no[10:14]} {self.account_no[14:18]} "
        f"{self.account_no[18:22]} {self.account_no[22:26]}"
    )
    formatted_balance = f"{self.balance:.2f}".replace(".", ",")
    print(f"Bank Account No: {formatted_no}")
    print(f"Balance: PLN {formatted_balance}\n")


def main():
  # i. Utworzenie konta
  account = BankAccount("12 3456 5555 9090 1111 0000 7722")

  # ii. Wyświetlenie salda
  account.display_info()

  # iii. Wpłata PLN 25,30
  account.deposit(25.30)

  # iv. Wyświetlenie salda
  account.display_info()

  # v. Wypłata PLN 31,70
  account.withdraw(31.70)

  # vi. Wyświetlenie salda
  account.display_info()

  # vii. Wypłata PLN 14
  account.withdraw(14)

  # viii. Wyświetlenie salda
  account.display_info()


if __name__ == "__main__":
  main()
