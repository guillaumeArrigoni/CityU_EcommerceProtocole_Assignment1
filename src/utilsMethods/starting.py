import src.cbc.cbc_encryption as cbcEncrypt
import src.ctr.ctr_encryption as ctrEncrypt
import src.cbc.cbc_decryption as cbcDecrypt


def isInputCorrect() :
    isInput_correct = input("Is the input correct? (yes/no)").lower()
    if isInput_correct == "yes" or "y":
        print("The process will start now.\n")
        isOk = True
    else :
        isOk = False
        print("The process will start again.\n")
    return isOk


def starting() :
    isOk = True
    print("Welcome !")
    while isOk :
        print("\nPlease choose an option: ")
        print("1 - CBC Encrypt")
        print("2 - CTR Encrypt")
        print("3 - CBC Decrypt")
        print("4 - Quit")
        userChoice = input("Please enter the number of the option you have choose.")
        print("\n")
        if userChoice == "1" :
            print("You have chosen the option: CBC Encryption")
            isCorrect = isInputCorrect()
            if isCorrect :
                cbcEncrypt.cbc_encryption()
        elif userChoice == "2" :
            print("You have chosen the option: CTR Encryption")
            isCorrect = isInputCorrect()
            if isCorrect :
                ctrEncrypt.ctr_encryption()
        elif userChoice == "3" :
            print("You have chosen the option: CBC Decryption")
            isCorrect = isInputCorrect()
            if isCorrect :
                cbcDecrypt.cbc_decryption()
        elif userChoice == "4" :
            print("You have chosen the option: Quit")
            isOk = not isInputCorrect()
        else :
            print("Error, the input is not correct. Please try again.\n")
            isOk = True
    print("\nGoodbye !")