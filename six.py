

                        # control Statement if and else
                    
                    # user voter adulat and not adulat

# n=int(input("Enter the age :"))

# if n>=18:
#     print("Adulat")
# else:
#     print("Not Adulat")


                            # WAP to check a number grade if and elif use

# num=int(input("Enter the number :"))

# if num>=90:
#     print("Grade : A")
# elif num>=80:
#     print("Grae : B")
# elif num>=70:
#     print("Grade : c")
# elif num>=60:
#     print("Grade : D")
# else:
#     print("Fail")


                            # WAP to chek number even or odd

# a=int(input("Enter a number :"))

# if a%2==0:
#     print("Even Number ")
# else:
#     print("Odd Number")



                                # WAP to traffic light a sinlge program


# light =input("Enter a light :")

# if light=="Green":
#     print("GO")
# elif light=="yellow":
#     print("start")
# else:
#     print("Stop")



        # circle radese

# n=int(input("Enter a number :"))
# area =3.14*n*n
# print(area)

# Move all zeros to the end without changing the order of other elements.

numbers = [0, 1, 0, 3, 12]

result = []
zero_count = 0

for num in numbers:
    if num == 0:
        zero_count += 1
    else:
        result.append(num)

for i in range(zero_count):
    result.append(0)

print("Original List:", numbers)
print("After Moving Zeros:", result)