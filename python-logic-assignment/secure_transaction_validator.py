balance = int(input("Enter your account balance: "))
withdrawal = int(input("Enter the withdrawal amount: "))
verification_input = input("Enter verification status (true/false): ").strip().lower()

if verification_input == "true":
    verified = True
elif verification_input == "false":
    verified = False
else:
    print("Transaction denied")
    exit()

if verified and withdrawal <= balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")
