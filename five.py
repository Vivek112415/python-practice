def call_sum():
    
    a=int(input("enter the number :"))
    b=int(input("enter the secound number :"))
    r=input("enter the operator (+,-,*,/): ")
    if r=='+':
        print("sum of two number is :",a+b)
    elif r=='-':
        print("subtraction of two number is :",a-b)
    elif r=='*':
        print("multiplication of two number is :",a*b)
    elif r=='/':
        print("division of two number is :",a/b)
    else:
        print("invalid operator")
    
call_sum()