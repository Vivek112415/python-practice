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
