from src.utilsMethods.askInformations import AskInformation
import src.utilsMethods.operation as operation



def cbc_encryption() :
    class_AskInformation = AskInformation()

    #Ask the user the information to perform the encryption
    dictionary_alphabet,dictionary_number_alphabet, IV, number_bits, k, userInput_encrypt = class_AskInformation.askInformation_v2()

    #Start to convert the user input text into binary
    binaryUserInput = []
    for letter in userInput_encrypt :
        if letter in dictionary_alphabet :
            binaryUserInput.append(dictionary_alphabet[letter])
        else :
            print("Error : some letter have no association.")
    print("The binary representation of the message is : " + str(binaryUserInput))

    #Start to perform the encryption
    XOR_list = [IV]
    XOR_list_shifted = [IV]
    finalAnswer = ""
    for i in range(len(binaryUserInput)):
        XOR_list.append(operation.xor_str(XOR_list_shifted[i], binaryUserInput[i]))
        XOR_list_shifted.append(operation.binaryDecimalAddition(XOR_list[i+1], k, len(dictionary_alphabet), number_bits))
        finalAnswer = finalAnswer + dictionary_number_alphabet[XOR_list_shifted[i+1]]
    print("The XOR list shifted is : " + str(XOR_list_shifted[1:]))

    print("The encrypted message is : " + finalAnswer)
