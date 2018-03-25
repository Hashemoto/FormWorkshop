import time
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
        balance = select_atm.withdraw_req(requested_money)
        if balance ==0:
            print "No more Widthraws can be done. \nYour current balance is Zero.\nThank you for using "+ select_atm.bank_name+" ATM"
            break
    if raw_input("Enter 'Y'es to see your Withdraw History : ")=="Y":
        select_atm.p_receipt()

class ATM():
    def __init__(self, acc_balance,bank_name):
        self.balance = int(acc_balance)
        self.bank_name = bank_name
        self.withdraw_list = []
        print "Welcome to "+self.bank_name
        print "Your Current Balance is : "+str(self.balance)
        print "=================================="

    def withdraw_req(self,request):
        if request > self.balance:
            print "Out of Balance, only "+str(self.balance)+" is availble for widthraw!"
        else:
            notes=[100,50,10,5,4,3,2,1]
            self.balance -= request
            for x in notes:
                while x <= request:
                    request -= x
                    print "Give "+str(x)
                    self.withdraw_list.append("Give "+str(x) +"  Was done on "+time.ctime())
            print "Remaining balance is : "+str(self.balance)
        print "=================================="
        return self.balance

    def p_receipt(self):
        if len(self.withdraw_list) == 0:
            print "\nYou did not do any withdraw request !"
            print "=================================="
        else:
            print "\nYour withdraw history is :"
            print "=================================="
            for i in self.withdraw_list:
                print i

balance1 =500
atm1 = ATM(balance1,"ADCB Bank")
prompt_request(atm1)
#atm1.withdraw_req(19)
