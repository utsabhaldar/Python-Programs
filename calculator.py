# Progarmme to make calculator in a simple way

num1=int(input("Enter the number 1 :  "))

num2=int(input("Enter the number 2 :  "))

oper=input("Enter the operator : ")

if oper=='+':
    result=num1+num2

elif oper=='-' :
    result=num1-num2

elif oper=='*' :
    result=num1*num2

elif oper=='/' :
    result=num1/num2
    
elif oper=='%' :
    result=num1%num2    

else:
    print("invalid Input ")    


print("The result is : ",result)




