
            # : Find the Second Largest Number
# numbers = [10, 25, 8, 45, 30]

# largest = numbers[0]
# second = numbers[0]

# for num in numbers:
#     if num > largest:
#         second = largest
#         largest = num
#     elif num > second and num != largest:
#         second = num

# print("Largest number:", largest)
# print("Second largest number:", second)


# class or object 

# class student:
#     def sum(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age) 

# s1=student()
# s1.sum("vivek",21)
# s1.sum("Chahal",22)
# s1.sum("shourya",23)


class student:
    def sum(self):
        self.name = "chahal"
        self.age = 21
        print(self.name,self.age) 
        print("vivek",22) 

s1=student()
s1.sum()

