
                # For loop 

        # WAP to use list print

# list=["C","C++","Java","Python","SQL"]

# for i in list:
#     print(i)


#                   WAP to use a list print while loop

# li=["c++","Java","PL/SQL","Science"]
# i=0
# while i<=4:
#     print(li[i])
#     i=i+1


                                # WAP to odd number add
# oddSum=0
# for i in range(10):
#         if i%2 != 0:
#                 oddSum = oddSum + i                    
# print("Odd number sum is :",oddSum)    

#                                 # WAP to even number add

# evenSum=0
# for i in range(10):
#         if i%2 == 0:
#                 evenSum = evenSum + i
# print("Even number sum is :",evenSum)


        #Sum of Multiples Write a for loop to calculate the sum of all numbers between 1 and 50 that are divisible by 3.

# multipleSum=0
# for i in range(1,51):
#         if i%3==0:
#                 multipleSum = multipleSum + i
# print("Sum of multiples of 3 between 1 and 50 is :",multipleSum)


# Given the list colors = ["red", "green", "blue", "yellow"], write a for loop that prints each color in reverse order without using the .reverse() method or list slicing [::-1].

# list =["red", "green", "blue", "yellow"]
# for i in range(len(list)-1,-1,-1):
#     print(list[i])


# Write a program that takes a string (e.g., text = "python programming") and uses a for loop to count how many times the letter "g" appears.

# text = "python programming"
# count = 0
# for char in text:
#         if char == "g":
#                 count += 1
# print("The letter 'g' appears :", count)


# factorial number 

# n=int(input("Enter a number: "))
# fact =1
# for i in range(1,n+1):
#     fact = fact * i
# print("Factorial of number ",fact)


# Positive, Negative, or Zero number check

# n=float(input("Enter a number: "))
# if n>0:
#         print("Positive number")
# elif n<0:
#         print("Negative number")
# else:
#         print("Zero")



                                # nested loop

# for i in range(1,11):
#         for j in range(1,11):
#                 print(i*j,end=" ")
#         print(' ')


        # mested while loop

# i=1
# while i<5:
#         j=1
#         while j<10:
#                 print(j,end=" ")
#                 j=j+1
#         print(' ')
#         i=i+1
#         print(' ')


                                # bracket loop

for i in range(1,6):
    if i==3:
        break
    print(i)


                                # continue loop

for i in range(1,6):
        if i==3:
                continue
        print(i)