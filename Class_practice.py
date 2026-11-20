#1
class Employee:
    def __init__(self,name,designation,salary):
        self.name=name
        self.designation=designation
        self.salary=salary
    def give_hike(self,percentage):
        hike=int(self.salary*(percentage/100))
        self.salary+=hike
        return f'{self.name} got a {percentage}% hike.New Salary:{self.salary}'
    def display_info(self):
        return f'{self.name}|{self.designation}|Salary:{self.salary}'
        
emp1_data = ("Ravi", "Data Engineer", 45000)
emp2_data = ("Sneha", "Python Developer", 52000)

e1=Employee(*emp1_data)
e2=Employee(*emp2_data)

print(e1.give_hike(10))
print(e1.display_info())
        
		
#2
class BankAccount:
    def __init__ (self,account_holder,opening_balance):
        self.account_holder=account_holder
        self.__balance=opening_balance
        
    def deposited(self,amount):
        self.__balance+=amount
        return f'Deposited {amount}. Balance :{self.__balance}'
        
    def withdraw(self,amount):
        if amount>self.__balance:
            return f'withdrawal Failed:Insufficient balance (Available: {self.__balance})'
        self.__balance-=amount
        return f'Withdraw {amount}.Balance:{self.__balance}'
            
    def get_balance(self):
        return f'{self.__balance}'
        
account_holder = "Divya"
opening_balance = 10000
transactions = [("deposit", 5000), ("withdraw", 3000), ("withdraw", 20000)]

Account=BankAccount(account_holder,opening_balance)


for action,amount in transactions:
    if action == "deposit":
        print(Account.deposited(amount))
    else:
        print(Account.withdraw(amount))


#3class Vehicle:
    def __init__(self,brand,rent_per_day,days):
        self.brand=brand
        self.rent_per_day=rent_per_day
        self.days=days
    def calulcate_rent(self):
        cal_rent=self.rent_per_day*self.days
        return cal_rent

class bike(Vehicle):
    pass

class Car(Vehicle):
    def calulcate_rent(self):
        base_rent=super().calulcate_rent()
        driver_charge=500*self.days
        return base_rent+driver_charge
    

Bike1=("Activa",400,2)
Bike2=("TVS",400,6)

Car1=("Maruthi",1500,3)
Car2=("Mahindra",2000,5)

r1=bike(*Bike1)
r2=bike(*Bike1)

c1=Car(*Car1)
c2=Car(*Car2)
print(f'Car({c1.brand}) Rent for {c1.days} days:',c1.calulcate_rent())
print(f'Bike({r1.brand}) Rent for {r1.days} days:',r1.calulcate_rent())

#4
class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def caluclate_bonus(self):
        return 0
class Manager(Employee):
    def calulcate_bonus(self):
        return self.base_salary*20/100
        
class Developer(Employee):
    def calulcate_bonus(self):
        return self.base_salary*12/100

mgr_data=('Suresh',70000)
dev_data=('Priya',55000)

mgr=Manager(*mgr_data)
dev=Developer(*dev_data)

employees=[mgr,dev]

for emp in employees:
    role=emp.__class__.__name__
    bonus=emp.calulcate_bonus()
    print(f'{emp.name}({role})->Bonus:{bonus}')
    
#5
from abc import ABC,abstractmethod

class paymentMethod(ABC):

    @abstractmethod
    def process_payment(self,amount):
        pass

try:
    pm=paymentMethod()
except TypeError as e:
    print(f"Error:{e}\n")

class UPI(paymentMethod):
    def process_payment(self,amount):
        print(f"[UPI] Rs.{amount} debited via UPI. Ref: UPI-TXN")
class CreditCard(paymentMethod):
    def process_payment(self,amount):
        print(f"[CreditCard] Charged Rs.{amount} successfully. Ref: CC-TXN")
class PayPal(paymentMethod):
    def process_payment(self,amount):
        print(f"[PayPal] Rs.{amount} processed via PayPal wallet. Ref: PP-TXN")

payments_to_process = [("CreditCard", 2500), ("UPI", 899), ("PayPal", 4200)]

payment_types = {"CreditCard": CreditCard, "UPI": UPI, "PayPal": PayPal}


for types,amount in payments_to_process:
    #obj=payment_types[types]()  
    #print(obj)
    print(f'{types}:{amount}')
    #print(amount)
    #obj.process_payment(amount)
    types=payment_types[types]()
    print(types)
    types.process_payment(amount)

        
        


