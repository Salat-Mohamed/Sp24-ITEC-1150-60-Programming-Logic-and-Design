def print_name_vertically():
    """Asks the user for their name, prints each letter vertically in uppercase,
       then prints a message with the name in its original case."""

    name = input("Enter your name: ")

    for letter in name:
        print(letter.upper())

    print("\nThat was your name vertically,", name + ". Thanks for using this program!")

if __name__ == "__main__":
    print_name_vertically()
