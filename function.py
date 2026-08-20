                        # even odd number user input
# def cal_sum():
#     n=int(input("Enter a number :"))
#     if n%2==0:
#         print("Even")
#     else:
#         print("Odd")
# cal_sum()

                        # even odd to list numbere

def cal_add(list):
    list=[1,22,43,55,22,11,33,13,7,56,96,44,5,3,6]
    odd=[]
    even=[]
    for i in list:
        if i % 2==0:
            even.append(i)
        else:
            odd.append(i)
    print("oringial list:",list)
    print("even number list:",even)
    print("odd number list:",odd)

cal_add(list)

