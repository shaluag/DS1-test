class Bank:
    # def __init__(self, name, pin , balance):
    #     self.name=name
    #     self.pin=pin
    #     self.balance=balance
    def __init__(self):
        self.name="Shalu"
        self.pin=0
        self.balance=0
        self.menu()
    
    def menu(self):
        user_input=input('''
        1. Press 1 for Generate Pin:
        2. Press 2 for Set Balance: 
        3. Press 3 for withdrawal: ''')
        if user_input == "1":
            self.set_pin() 
        if user_input == "2":
            self.set_balance()
        if user_input =="3":
            self.withdrawal()
    
    def set_pin(self):
        new_pin=input("Enter your pin: ")
        self.pin = new_pin
        self.menu()


    def set_balance(self):
        new_balance=input("Enter Amount:")
        self.balance = new_balance
        self.menu()
    
    def withdrawal(self):
        pin=input("Enter your pin: ")
        if self.pin == pin:
            amount=int(input("Enter withdrawal amount: "))
            if amount > self.balance:
                print("Insufficient balance")
                exit()
            else:
                self.balance=self.balance-amount
                print("Withdrawal successful")
                print("Current Blance: ", self.balance)
            
B1=Bank()

