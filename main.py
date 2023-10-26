

#Carson Hernandez
from Encoder import encoder

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

            print(f"The encoded password is {grape_fruit}, and the original password is PUT DECODER HERE\n ")


if __name__ == "__main__":
    menu()