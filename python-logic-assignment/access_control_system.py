age = int(input("Enter your age: "))
id_input = input("Enter the True or False: ").strip().lower()

if id_input == "true":
    has_id = True
elif id_input == "false":
    has_id = False
else:
    print("Invalid ID input")
    exit()

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
