name = input("Enter your name: ")
age = int(input("Enter your age: "))
active_input = input("Are you an active user (True/False): ")

is_active = active_input == "True"

print(f"User {name} is {age} years old. Active status: {is_active}")
