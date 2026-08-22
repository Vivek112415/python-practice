

# for i in range(1,5):
#         print("x" *i)



# for i in range(4, -1,-1):
#     print("x" *i)


# # Number Pyramid Pattern

# n =5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

"""""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print()


"""
5, 4, 3, 2, 1
4, 3, 2, 1
3, 2, 1
2, 1
1
"""
n = 5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    