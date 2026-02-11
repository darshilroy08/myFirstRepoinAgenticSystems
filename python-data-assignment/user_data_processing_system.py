def calculate_average(scores):
    """Calculate and return average score from a list of integers."""
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


def has_admin_access(roles):
    """Return True if 'admin' role exists, otherwise False."""
    return "admin" in roles


def main():
    users = [
        {
            "name": "Alice",
            "scores": [85, 90, 78],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Bob",
            "scores": [70, 75, 80],
            "roles": {"viewer"}
        },
        {
            "name": "Charlie",
            "scores": [88, 92, 84],
            "roles": {"editor", "viewer"}
        }
    ]

    for user in users:
        name = user["name"]
        scores = user["scores"]
        roles = user["roles"]

        average_score = calculate_average(scores)
        admin_status = has_admin_access(roles)

        print("Name:", name)
        print("Average Score:", round(average_score, 2))
        print("Admin Access:", admin_status)
        print("-" * 30)

main()
