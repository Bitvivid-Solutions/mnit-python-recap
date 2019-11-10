def get_non_negative_int(prompt):
    while True:
        value = input(prompt)
        if not value:
            print("It cannot be empty")
            continue
        try:
            value = int(value)
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value




def get_string_value(prompt):
    while True:
        value = input(prompt)
        if not value:
            print("It cannot be empty")
            continue
        try:
            value = int(value)
            print("Sorry, I didn't understand that.")
            continue

        except ValueError:
            # if it gives value error then it must have failed to convert int into string.
            return value

