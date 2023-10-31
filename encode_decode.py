""" Encode and decode an 8-digit pin
This is done with a Caesar cipher, rotated up by 3 for each digit"""


# By Anthony Thisse
# Encode a password
def encode(unencoded_password):
    encoded_password = ""
    try:
        # For each digit in the password, shift the digit up by 3
        for i in unencoded_password:
            encoded_password += str((int(i) + 3) % 10)
        # Print a success message
        print("Your password has been encoded and stored!")
        return encoded_password

    # Test for bad input (password must be not empty and must only be ints)
    except (ValueError, EOFError):
        print("Please enter a password with only integers. Your password has not been encoded.")
        return ""


# Decode a password
def decode(encoded_password):
    decoded_pass = ""
    for i in encoded_password:
        if int(i) < 3:
            i = int(i) + 10
        original_digit = int(i) - 3
        decoded_pass = decoded_pass + str(original_digit)

    return decoded_pass


# Print the menu and get the user's choice
def print_menu_and_get_input():
    user_input = -1
    valid_input = False
    # Print the menu
    print("Menu")
    print(13 * "-")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

    # While the input is invalid
    while not valid_input:
        try:
            # Get the user's option
            user_input = int(input("Please enter an option: "))

            # Raise an error if the input is invalid
            if user_input < 1 or user_input > 3:
                raise ValueError  # Perhaps this should be a custom error named InvalidOption
            valid_input = True

        # If the input is invalid, tell the user what to do
        except (ValueError, EOFError):
            print("Please enter an option 1-3.")
    return user_input


# Print the menu
def main():
    user_input = -1
    encoded_password = ""

    # While the user doesn't want to exit
    while user_input != 3:
        # Print the menu and get the input
        user_input = print_menu_and_get_input()

        # Encode a password
        if user_input == 1:
            encoded_password = encode(input("Please enter your password to encode: "))

        # Decode a password
        if user_input == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

    # Exit with normal code
    exit(0)


if __name__ == "__main__":
    main()
