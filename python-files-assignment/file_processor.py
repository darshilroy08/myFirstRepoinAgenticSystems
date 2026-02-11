numbers = []

# Reading the file
with open("python-files-assignment/numbers.txt", "r") as file:
    print("File opened successfully")
    for line in file:
        clean_line = line.strip()
        if clean_line:  # ignore empty lines
            numbers.append(int(clean_line))

print(f"Read {len(numbers)} numbers")

# Computation
total_values = len(numbers)
total_sum = sum(numbers)

if total_values > 0:
    average_value = total_sum / total_values
else:
    average_value = 0

# Writing logs (append mode)
with open("results.log", "a") as log_file:
    log_file.write("File opened successfully\n")
    log_file.write(f"Read {total_values} numbers\n")
    log_file.write(f"Sum: {total_sum}\n")
    log_file.write(f"Average: {average_value}\n")
    log_file.write("Processing completed\n\n")

print("Processing completed")
