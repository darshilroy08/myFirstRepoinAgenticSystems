accuracy_input = input("Enter model accuracy: ")

if accuracy_input.replace('.', '', 1).isdigit():
    accuracy = float(accuracy_input)
    print(f"Model accuracy is {accuracy}")
else:
    print("Invalid input. Please enter a numeric value.")
