import time


class BalanceExceptionError(Exception):
    pass


class AttemptExceptionError(Exception):
    pass


attempt = 1

class sampleclass:
    def withdraw():
        global attempt
        balance = 10000
        saved_pin = 1234
        pin = int(input("enter the pin :"))
        if pin == saved_pin:
            try:
                amt = float(input("enter the amt to withdraw :"))
                temp_bal = balance - amt
                if temp_bal < 1000:
                    raise BalanceExceptionError("insufficient balance")
                balance = balance - amt
                print("Remaining balance :", balance)
            except Exception as err:
                print(err)

        else:
            ans = input("WRONG PIN : Do u want to continue :(Y/N) :")
            if ans.lower() == 'y':
                attempt += 1
                try:
                    if attempt == 4:
                        raise AttemptExceptionError("too many try")
                except Exception as err:
                    print(err)
                    time.sleep(3)
                else:
                   sampleclass.withdraw()
            else:
                print("Thank You")
                # return


obj=sampleclass
print(obj.withdraw())
