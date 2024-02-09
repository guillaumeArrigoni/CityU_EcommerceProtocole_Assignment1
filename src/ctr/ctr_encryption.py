from src.utilsMethods.askInformations import AskInformation
import src.utilsMethods.operation as operation


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

#Start to perform the encryption
print("The binary representation of the message is : " + str(binaryUserInput))
XOR = []
IV_shifted = []
finalAnswer = ""
for i in range(len(binaryUserInput)):
    IV_shifted.append(operation.binaryDecimalAddition(IV, int(k)+int(i), len(dictionary_alphabet), number_bits))
    XOR.append(operation.xor_str(binaryUserInput[i], IV_shifted[i]))
    finalAnswer = finalAnswer + dictionary_number_alphabet[XOR[i]]
print("The IV shifted is : " + str(IV_shifted))
print("The XOR list is : " + str(XOR))

print("The encrypted message is : " + finalAnswer)
