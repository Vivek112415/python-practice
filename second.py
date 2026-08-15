def find_name(name,target):
    left=0
    right=len(name)-1

    while left<=right:
        middle =(left + right)//2

        if name[middle]==target:
            return middle
        elif name [middle]<target:
                left =middle+1
        else:
                right =middle -1

    return -1
name=["John", "Alice", "Bob", "Charlie", "David"]

target_name = "chahal"
result = find_name(name, target_name)

if result != -1:
    print("found at index:", result)
else:
    print("not found")


def paper_fint(name,paper):
    for paper in paper:
        if paper==name:
            return True
    return False

paper=["John", "Alice", "Bob", "Charlie", "David"]

search_name = "Alice"

result = paper_fint(search_name, paper)
if result:
    print("found")
else:
    print("not found")

#                           Duplicate value

def duplicate_value(number):
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            if i !=j and number[i] == number[j]:
                return True
    return False
number=[1,2,3,4,5,6,7,8,9,10]

result=duplicate_value(number)
if result:
    print("duplicate value found")
else:
    print("no duplicassste value found")
