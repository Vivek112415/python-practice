

#                         # even odd to list numbere

# def cal_add(list):
#     list=[1,22,43,55,22,11,33,13,7,56,96,44,5,3,6]
#     odd=[]
#     even=[]
#     for i in list:
#         if i % 2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     print("oringial list:",list)
#     print("even number list:",even)
#     print("odd number list:",odd)

# cal_add(list)

#                         # user input to list number

# def cal_add(list):
#     list=[]
#     n=int(input("enter the number of elements:"))
#     for i in range(10):
#         ele=int(input("enter the element:"))
#         list.append(ele)
#     odd=[]
#     even=[]
#     for i in list:
#         if i % 2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     print("oringial list:",list)
#     print("even number list:",even)
#     print("odd number list:",odd)

# cal_add(list)


                        # Recursion to function

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)

# print("Factorial of number is:",fact(5))


                # recursion to factorial number to user input

# def fact_su(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact_su(n-1)

# n=int(input("Enter a number: "))
# print("Factorial of number is:",fact_su(n))


                    # lambda function

# fun = lambda x: x*x
# print(fun(5))


                # lambda function to user input
# x = int(input("Enter a number: "))
# fun = lambda x: x*x
# print(fun(x))


                # lambda function to add two number

# fun =lambda x,y : x+y
# print(fun(5,6))

                # multi value return to function

# def cal_add(a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return sum,sub,mul,div
# a,b,c,d = cal_add(10,5)
# print("sum is:",a)
# print("sub is:",b)
# print("mul is:",c)
# print("div is:",d)



# pre define function

# print(len("hello world"))

# find the maximum value
# print(max(10,20,30,40,50))

# min value function pre define

# print(min(1,20,30,40,50))