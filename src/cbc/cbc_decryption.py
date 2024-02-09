from src.utilsMethods.askInformations import AskInformation
import src.utilsMethods.operation as operation


class_AskInformation = AskInformation()

#Ask the user the information to perform the encryption
dictionary_alphabet,dictionary_number_alphabet, IV, number_bits, k, userInput_encrypt = class_AskInformation.askInformation_v2()

#Start to convert the user input text into binary
binaryUserInput = [IV]
for letter in userInput_encrypt :
    if letter in dictionary_alphabet :
        binaryUserInput.append(dictionary_alphabet[letter])
    else :
        print("Error : some letter have no association.")
print("The binary representation of the message is : " + str(binaryUserInput[1:]))

#Start to perform the encryption
soustrait = []
for i in range(1,len(binaryUserInput)):
    soustrait.append(operation.binaryDecimalAddition(binaryUserInput[i], int(-int(k)), len(dictionary_alphabet), number_bits))
XOR_list = [IV]
finalAnswer = ""
for i in range(1,len(binaryUserInput)):
    XOR_list.append(operation.xor_str(binaryUserInput[i-1], soustrait[i-1]))
    finalAnswer = finalAnswer + dictionary_number_alphabet[XOR_list[i]]
print("The soustrait list is : " + str(soustrait))
print("The XOR list is : " + str(XOR_list))

print("The encrypted message is : " + finalAnswer)
