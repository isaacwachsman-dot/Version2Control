#Lab 6 - Isaac Wachsman

#String Encoder Function
def encode(string):
    newStr = ""
    #Iterates through characters in string: adds 3, then takes modulo 10
    for i in string:
        newStr += str((int(i)+3)%10)

    return newStr


def decode(string):
    newStr = ""
    #Iterates through characters in string: adds 3, then takes modulo 10
    for i in string:
        newStr += str((int(i)-3)%10)

    return newStr


#Main Function
def main():
    #Print out the menu with options
    print("Menu")
    print("-"*13)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    choice = 0
    #Check if user has quit
    while choice != "3":
        #Ask for user input
        choice = input("Please enter an option:")
        #Check if user chose encode
        if choice == "1":
            password = input("Please enter your password to encode:")
            #Encode password
            password = encode(password)
            print("Your password has been encoded and stored!")
        #Check if user chose decode
        elif choice == "2":
            #Print encoded password and decoded password
            print(f'The encoded password is {password}, and the original password is {decode(password)}.')


#Run main
if __name__ == "__main__":
    main()
