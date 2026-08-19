
users_db = {}

# Kitne users add karne hain
num_users = int(input("How many users do you want to add? "))

# Users ka data input lene ke liye loop
for i in range(num_users):
    print(f"\n--- User {i + 1} Details ---")
    user_id = input("Enter User ID: ")
    user_name = input("Enter User Name: ")
    user_age = input("Enter User Age: ")

    # Dictionary mein user_id ko KEY banakar baki details store kar rahe hain
    users_db[user_id] = {
        "Name": user_name,
        "Age": user_age
    }

print("\n" + "="*40)

# Particular user ki details search karne ke liye
search_id = input("\n Enter your user id : ")

# Search result check karna
if search_id in users_db:
    print("\n--- User Details Found ---")
    print(f"User ID : {search_id}")
    print(f"Name    : {users_db[search_id]['Name']}")
    print(f"Age     : {users_db[search_id]['Age']}")
else:
    print(f"\nError: '{search_id}' ID wala koi user nahi mila.")