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

def widthraw_req(balance,request):
    new_balance = balance -request
    while request > 0:
        if balance < request:
            print "Out of Balance, only "+str(balance)+" is availble for widthraw!"
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
    return new_balance

balance =500
while raw_input("if you Want to widthraw please enter 'Y' : ") =="Y":
    request = input_request()
    balance = widthraw_req(balance,request)
    if balance ==0:
        print "Your Balance Reached Zero."
        break
