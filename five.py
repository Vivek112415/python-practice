# def call_sum():
#     # =============Calculator========================

#     a=int(input("enter the number :"))
#     b=int(input("enter the secound number :"))
#     r=input("enter the operator (+,-,*,/): ")
#     if r=='+':
#         print("sum of two number is :",a+b)
#     elif r=='-':
#         print("subtraction of two number is :",a-b)
#     elif r=='*':
#         print("multiplication of two number is :",a*b)
#     elif r=='/':
#         print("division of two number is :",a/b)
#     else:
#         print("invalid operator")
# call_sum()


          #array



def sum_su(a):
    

    # ============sum of array========================
    print("sum of array is :",sum(a))

    # ===========max of array========================
    print("max of array is :",max(a))

    # ===========min of array========================
    print("min of array is :",min(a))

    # ===========length of array========================
    print("length of array is :",len(a))

    # ===========count of array========================
    print("count of array is :",a.count(3))

    # ===========sort of array========================
    a.sort()
    print("sort of array is :",a)

    # ===========reverse of array========================
    a.reverse()

    # ==========reverse of array========================
    print("reverse of array is :",a)

    # =========append of array========================
    a.append(100)
    print("append of array is :",a)

    # =========insert of array========================
    a.insert(2,100)
    print("insert of array is :",a)

a=[1,2,2,8,3,4,43,3,2,5]
sum_su(a)