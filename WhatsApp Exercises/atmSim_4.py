class user:
    _balance = 50.0

    def getBalance(self):
        return self._balance
    
    def setBalance(self,amount):
        self._balance = self.getBalance() + amount

class ATM:
    def deposit(self, user, amount):
        if amount%5 == 0 and amount > 0:
            user.setBalance(amount)
        else: print("Incorect amount")

    def withdraw(self, user,amount):
        if amount%5 == 0 and amount<0.00:
            if user.getBalance() >= amount*-1:
                user.setBalance(amount)
            else:
                print("Error, balance")
        else:
            print("incorrect amount")
    def showBalance(self, user):
        print(user.getBalance())


u = user()
atm = ATM()

atm.showBalance(u)
atm.deposit(u,0.2)
atm.showBalance(u)
atm.withdraw(u,-5)
atm.showBalance(u)

#atm.deposit(u,-10)
#print(u.getBalance())
