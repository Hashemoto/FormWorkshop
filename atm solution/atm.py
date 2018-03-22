def input_request ():
    user_prompt = "Please enter the value to widthraw in numbers! : "
    try:
        input = int(raw_input(user_prompt))
    except:
        print "Entered Value is not a Number!!!!!!!!!!"
    print "you have entered this value "+str(input)
    if input <= 0:
        print "Value should be more than Zero"
        return 0
    return input

money_in_atm =500
request =input_request()
while request > 0:
    if money_in_atm <request:
        print "a maximum value of "+str(money_in_atm)+" can only be requested !"
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
