class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin

    def balance(self):
        print("your balance is 50000")

    def withdraw(self,amount):
        newAmount=50000-amount
        print("you have withdraw"+str(amount)+"your balance is"+str(newAmount))

def main():
    cardnumber=input("enter your card number")
    pin=input("enter your pin")
    new_user=Atm(cardnumber, pin)

    print("select an option")
    print("1 balance inquiry")
    print("2 cash withdraw")
    option = int(input("select option"))
    
    if(option==1):
        new_user.balance()
    elif (option==2):
        amount=int(input("enter an amount"))  
        new_user.withdraw(amount)
    else:
        print("select correct option")  
