class  NextVault:
    def __init__(self):
        self.balance = 0
        

    def deposit(self):
            amount = float(input('eneter amount to deposit'))
            self.balance = self.balance + amount
            print('transaction successful!!!')

    def transfer(self):
            amount = float(input('enter amount to transfer'))
            if amount >self.balance or amount == 0:
                print('insufficient funds ')
                print('transaction failed')
            else:
                account_number = input('enter customer account number')
                bank =input('enter customer bank name')
                self.balance = self.balance - amount
                print('transaction successful')
                

    def buy_airtime(self):
            amount = float(input('enter airtime amount'))
            if amount >self.balance or amount ==0:
                print('insufficient funds ')
                print('transaction failed')
            else:
                phone_number = input('enter customer account number')
                network =input('enter customer network')
                self.balance = self.balance - amount
                print('transaction successful')

    def buy_data(self):
            amount = float(input('enter data amount'))
            if amount >self.balance or amount ==0:
                print('insufficient funds ')
                print('transaction failed')
            else:
                phone_number = input('enter customer account number')
                network =input(' enter customer network')
                self.balance = self.balance - amount
                print('transaction successful')
    def check_balance(self):
            print('your current balance is',self.balance)
  