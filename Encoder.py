
#Carson Hernandez
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