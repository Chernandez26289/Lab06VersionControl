def decode(encoded_string):
    for i in encoded_string:

        if i == "0":
            encoded_string = encoded_string.replace("0","7")

        if i == "1":
            encoded_string = encoded_string.replace("1", "8")

        if i == "2":
            encoded_string = encoded_string.replace("2", "9")

        if i == "3":
            encoded_string = encoded_string.replace("3", "0")

        if i == "4":
            encoded_string = encoded_string.replace("4", "1")

        if i == "5":
            encoded_string = encoded_string.replace("5", "2")

        if i == "6":
            encoded_string = encoded_string.replace("6", "3")

        if i == "7":
            encoded_string = encoded_string.replace("7", "4")

        if i == "8":
            encoded_string = encoded_string.replace("8", "5")

        if i == "9":
            encoded_string = encoded_string.replace("9", "6")

            return encoded_string

    return encoded_string
def encoder(password):

    encoded_string = str(password)

    for i in encoded_string:

        if i == "0":
            encoded_string = encoded_string.replace("0","3")

        if i == "1":
            encoded_string = encoded_string.replace("1", "4")

        if i == "2":
            encoded_string = encoded_string.replace("2", "5")

        if i == "3":
            encoded_string = encoded_string.replace("3", "6")

        if i == "4":
            encoded_string = encoded_string.replace("4", "7")

        if i == "5":
            encoded_string = encoded_string.replace("5", "8")

        if i == "6":
            encoded_string = encoded_string.replace("6", "9")

        if i == "7":
            encoded_string = encoded_string.replace("7", "0")

        if i == "8":
            encoded_string = encoded_string.replace("8", "1")

        if i == "9":
            encoded_string = encoded_string.replace("9", "2")

            return encoded_string

    return encoded_string

def menu():
    Continue = True
    while Continue == True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n ")
        choice = int(input("Please enter an option: "))

        if choice == 1:

            password_nonencoded = int(input("Please enter your password to encode: "))

            print("Your password has been encoded and stored!\n ")

            grape_fruit = encoder(password_nonencoded)

        if choice == 2:

            #CALL DECODER HERE THEN INPUT THE VALUE IN F STRING:)
            orange = decode(grape_fruit)

            print(f"The encoded password is {grape_fruit}, and the original password is {orange}" )

if __name__ == "__main__":
    menu()