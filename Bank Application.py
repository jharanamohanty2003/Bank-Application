class Bank():
    IFSC='BANK000420'
    ROI=0.07
    def __init__(self,name,accno,bal,mobno,pin):
        self.name=name
        self.accno=accno
        self.bal=bal
        self.mobno=mobno
        self.pin=pin
    def display_details(self):
        print(f'Name={self.name}')
        print(f'Acc Number={self.accno}')
        print(f'Mobile={self.mobno}')
    def withdraw(self):
        attempts=3
        while attempts>0:
            print(f'No. of chances is {attempts}')
            if self.getpassword()==self.pin:
                amount=int(input('enter the amount to withdraw:'))
                if amount<=self.bal:
                    if amount%100==0:
                        if 500<=amount<=10000:
                            self.bal-=amount
                            print('Amount debited successfully')
                            print(f'Avl Bal is {self.bal}')
                            break
                        else:
                            print('enter valid amount')
                    else:
                        print('no denominations')
                else:
                    print('Insufficient funds')
            else:  
               print('Invalid Password')
        else:
            print('No chances')
            print('Try after 24 hours')
    def deposit(self):
         if self.accno==int(input('enter account number:')):
             amount=int(input('enter the amount to deposite:'))
             if amount%100==0:
                 if 100<=amount<=50000:
                     self.bal+=amount
                     print('Amount credited successfully')
                     print(f'Avl Bal is {self.bal}')
                 else:
                     print('Invalid amount')
             else:
                print('Invalid Denominations')
         else:
            print('Invalid acc number')
    def check_balance(self):
        attempts=3
        while attempts>0:
            print(f'No. of chances is {attempts}')
            if self.getpassword()==self.pin:
                print(f'Avl Bal is {self.bal}')
                break
            else:
                print('Invalid pin')
                attempts-=1
                print('-----------')
        else:
           print('no chances')
           print('Try after 24 hours')
    @classmethod
    def changeROI(cls):
        cls.ROI=0.08
    @staticmethod
    def getpassword():
        password=int(input('enter 4-digit pin='))
        return password
cust1=Bank('user1',1234567890,10000,9876543210,1111)
cust2=Bank('user2',1234560000,29999,9999999999,2222)
cust3=Bank('user3',1234570000,50000,9999999998,3333)
cust2.display_details()
cust3.display_details()
cust3.deposit()



        
             
