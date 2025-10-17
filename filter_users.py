import json

def filter_users_by_name(name):
    """Finds users by name and returns a list of matches """
    with open("users.json", "r") as file:
        users = json.load(file)
    return [user for user in users if user["name"].lower() == name.lower()]


def filter_users_by_age(age):
    """Finds users by age and returns a list of matches """
    with open("users.json", "r") as file:
        users = json.load(file)
    return [user for user in users if user["age"] == int(age)]


def filter_by_email(email):
    """Finds users by email and returns a list of matches."""
    with open("users.json", "r") as file:
        users = json.load(file)
    return [user for user in users if user["email"].lower() == email.lower()]


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? ('name', 'age', or 'email'): ").strip().lower()

    matching_users = []  # Start with an empty list

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        matching_users = filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = input("Enter age to filter users: ").strip()
        matching_users = filter_users_by_age(age_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter email to filter users: ").strip()
        matching_users = filter_by_email(email_to_search)
    else:
        print("Filtering by that option is not supported.")

    # Display the results
    # Only check results if the option was valid in the first place
    if filter_option in ["name", "age", "email"]:
        if matching_users:
            print("\nFound matching users:")
            for user in matching_users:
                print(f"Name: {user['name']} / Age: {user['age']} / Email: {user['email']} ✅")
        else:
            print("No match were found ❌")