import datetime
import pytz


class Account_Number:

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for {}".format(self.name))
        self.transaction_list.append((Account_Number._current_time(),balance))

    def deposit(self, amount):
        if (amount > 0):
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account_Number._current_time(),amount))

    def withdraw(self, amount):
        if (0 < amount <= self.balance):
            self.balance -= amount
            self.transaction_list.append((Account_Number._current_time(), -amount))
        else:
            print("Amount is more than your balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                trans_type ="Deposited"
            else:
                trans_type="Withdrawl"
                amount *= -1
            print("{:6} {} on {} (Local Time was {})".format(amount, trans_type, date, date.astimezone()))

def main():
# if __name__=="__main__":
    rabin = Account_Number("Rabin",0)
    rabin.show_balance()
    rabin.deposit(1000)

    rabin.withdraw(500)
    rabin.withdraw(501)
    #rabin._current_time()
    rabin.show_transactions()

    steph = Account_Number("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
main()
