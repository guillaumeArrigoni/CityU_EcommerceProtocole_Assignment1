

class AskInformation:
    def __init__(self):
        pass

    def askAlphabetNumberbits_v1(self):
        self.dictionary_alphabet_number = {}
        self.dictionary_number_alphabet = {}
        isOk = True
        while isOk:
            self.lenth_alphabet = input("Please enter the lenth of the alphabet: ")
            self.number_bits = input("Please enter the number of bits: ")
            for i in range(int(self.lenth_alphabet)):
                userInput_letter = input("Please enter the " + str(i) + " letter: ")
                userInput_binary = input("Please enter the binary representation of the letter: ")
                self.dictionary_alphabet_number[userInput_letter] = userInput_binary
                self.dictionary_number_alphabet[userInput_binary] = userInput_letter
            print("Here is the alphabet's association you have entered: ")
            print(self.dictionary_alphabet_number)
            print("Number of bits: " + self.number_bits)
            userInput_isOk = input("Is it correct? (yes/no)").lower()
            if userInput_isOk == "yes" or "y":
                isOk = False
            else:
                isOk = True
                self.dictionary_alphabet_number = {}
                self.dictionary_number_alphabet = {}
                print("The process will start again.\n")

    def askAlphabetNumberbits_v2(self):
        self.dictionary_alphabet_number = {}
        self.dictionary_number_alphabet = {}
        isOk = True
        while isOk:
            self.lenth_alphabet = input("Please enter the lenth of the alphabet: ")
            self.number_bits = input("Please enter the number of bits: ")
            startingLetter = input("Please enter the first letter of the alphabet: ")
            for i in range(int(self.lenth_alphabet)):
                letter = chr(ord(startingLetter) + i).upper()
                number = format(i, 'b').zfill(int(self.number_bits))
                self.dictionary_number_alphabet[number] = letter
                self.dictionary_alphabet_number[letter] = number
            print("Here is the alphabet's association you have entered: ")
            print(self.dictionary_alphabet_number)
            print("Number of bits: " + self.number_bits)
            userInput_isOk = input("Is it correct? (yes/no)").lower()
            if userInput_isOk == "yes" or "y":
                isOk = False
            else:
                isOk = True
                self.dictionary_alphabet_number = {}
                self.dictionary_number_alphabet = {}
                print("The process will start again.\n")

    def askIVShift(self):
        isOk = True
        while isOk:
            self.IV = input("Please enter the IV: ")
            self.k = input("Please enter the shift: ")
            print("Here is the information you have entered: ")
            print("IV: " + self.IV)
            print("Shift: " + self.k)
            if len(self.IV) != int(self.number_bits) or len(str(self.dictionary_alphabet_number[list(self.dictionary_alphabet_number.keys())[0]])) != int(self.number_bits):
                print("The IV, the alphabet's binary representation and the number of bits must have the same size.")
                isOk = True
                print("The process will start again.\n")
            else:
                userInput_isOk = input("Is it correct? (yes/no)").lower()
                if userInput_isOk == "yes" or "y":
                    isOk = False
                else:
                    isOk = True
                    print("The process will start again.\n")

    def askText(self):
        isOk = True
        while isOk:
            self.userInput_encrypt = input("Please enter the text you want to encrypt :").upper()
            print("Here is the information you have entered: ")
            print(self.userInput_encrypt)
            userInput_isOk = input("Is it correct? (yes/no)").lower()
            if userInput_isOk == "yes" or "y":
                isOk = False
            else:
                isOk = True
                print("The process will start again.\n")


    def askInformation_v1(self) :
        self.askAlphabetNumberbits_v1()
        self.askIVShift()
        self.askText()
        return self.dictionary_alphabet_number, self.dictionary_number_alphabet, self.IV, self.number_bits, self.k, self.userInput_encrypt

    def askInformation_v2(self) :
        self.askAlphabetNumberbits_v2()
        self.askIVShift()
        self.askText()
        return self.dictionary_alphabet_number, self.dictionary_number_alphabet, self.IV, self.number_bits, self.k, self.userInput_encrypt
