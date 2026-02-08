def greet_student(name):
    return f"Hello, {name}"

def calculate_scores(scores):
    total_subjects = len(scores)
    average_score = sum(scores) / total_subjects
    return total_subjects, average_score

def evaluate_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    name = "Alice"
    scores = [60, 70, 65]

    greeting = greet_student(name)
    subjects, average = calculate_scores(scores)
    result = evaluate_result(average)

    print(greeting)
    print(f"Subjects: {subjects}")
    print(f"Average Score: {average}")
    print(f"Result: {result}")

main()
