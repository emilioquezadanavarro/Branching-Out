import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users_age = [user for user in users if user["age"] == int(age)]

    return filtered_users_age


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? (Currently,'name' and 'age' are supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)


    elif filter_option == "age":
        age_to_search = input("Enter age to filter users: ").strip()
        # Call the function and get the list of matching users
        matching_users = filter_users_by_age(age_to_search)
        # Check if the list has anything in it.
        # An empty list evaluates to False in an if statement.
        if matching_users:
            # If it's not empty, loop through and print each user
            for user in matching_users:
                print(user)
        else:
            # If it's empty, print the message
            print("No match were found")
    else:
        print("Filtering by that option is not yet supported.")
