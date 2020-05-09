# try...except


def func1():
    while True:
        print("This is a division program.")
        c = input("Input 'c' continue, otherwise logout:")
        if c == 'c':
            a = input("first number:")
            b = input("second number:")
            try:
                print(f"{a}/{b} =", round(float(a)/float(b), 2))
                print('#'*33)
            except ZeroDivisionError:
                print("The second number cann't be Zero!")
                print('*'*33)
            except ValueError as ex:
                print("Please input number!")
                print(ex)
                print('*'*33)
            else:
                print("+"*33)
                break
            finally:
                print("-"*33)
        else:
            break

class Account():
    def __init__(self, number):
        self.number = number
        self.balance = 0

    def desposit(self,amount):
        try:
            assert amount >0
            self.balance += amount
        except:
            print("The money should be bigger than zero.")
    
    def withdraw(self,amount):
        assert amount > 0
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Balance is not enough.")


if __name__ == "__main__":
    # func1()
    a = Account(100)
    a.desposit(10)
    a.withdraw(120)
