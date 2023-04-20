def prnthex():
    # Prompt the user to enter a character
    a = input("Enter a character: ")
    # Convert the character to its corresponding ASCII code using ord()
    # Then convert the ASCII code to a hexadecimal string using hex()
    b = hex(ord(a))
    # Display the hexadecimal string
    print("This is the Hexadecimal Format: ",b)

    def verify():
        q = input("Would you like to check your answer? (y/n): ")
        if q == "y":

            # Convert the hexadecimal string to a character using chr()
            # Since it is a hexadecimal string, we need to convert it to an integer first
            # Then convert the integer to a character using chr()
            # Since the integer is in hexadecimal format, we need to specify the base as 16
            print("Is this your card?")
            print(chr(int(b, 16)))
        elif q == "n":
            print("Okay, bye!")
        else:
            print("Invalid input, please try again.")
            verify()
    verify()


def main():
    prnthex()

main()


