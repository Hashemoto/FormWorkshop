def input_request ():
    user_prompt = "Please enter the value to widthraw in numbers! : "
    try:
        input = int(raw_input(user_prompt))
    except:
        print "Requested Value is not a Number."
    if input <= 0:
        print "Requested Value should be more than Zero."
        return 0
    return input

def prompt_request(select_atm):
    while raw_input("if you Want to widthraw please enter 'Y' : ") =="Y":
        requested_money = input_request()
        balance = select_atm.widthraw_req(requested_money)
        if balance ==0:
            print "No more Widthraws can be done. \nYour current balance is Zero.\nThank you for using "+ select_atm.bank_name+" ATM"
            break


class ATM():
    def __init__(self, acc_balance,bank_name):
        self.balance = int(acc_balance)
        self.bank_name = bank_name
        print "Welcome to "+self.bank_name
        print "Your Current Balance is : "+str(self.balance)
        print "=================================="

    def widthraw_req(self,request):
        new_balance = self.balance - request
        while request > 0:
            if request > self.balance:
                print "Out of Balance, only "+str(self.balance)+" is availble for widthraw!"
                new_balance += request
                break
            if request >=100:
                print "Give 100"
                request -= 100
            elif request >= 50:
                print "Give 50"
                request -= 50
            elif request >= 10:
                print "Give 10"
                request -=10
            elif request >=5:
                print "Give 5"
                request -= 5
            elif request >0:
                print "Give "+str(request)
                request =0
        self.balance = new_balance
        print "Remaining balance is : "+str(self.balance)
        print "=================================="
        return self.balance

balance1 =500
atm1 = ATM(balance1,"ADCB Bank")
prompt_request(atm1)
#atm1.widthraw_req(19)
