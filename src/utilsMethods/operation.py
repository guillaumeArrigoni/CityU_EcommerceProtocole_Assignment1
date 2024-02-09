def xor_int(number1: int, number2: int):
    """
    Method use to perform the XOR operation between two integers

    :param number1: The first number use to perform the XOR operation
    :type number1: int
    :param number2: The second number use to perform the XOR operation
    :type number2: int

    :return: The result of the XOR operation
    :rtype: str
    """
    number1_str = str(max(number1, number2))
    number2_str = str(min(number2, number1))
    xor = ""
    for i in number1_str:
        if i > len(number2_str) - 1:
            print("Error, the input must be the same size")
        else:
            if number1_str[i] == number2_str[i]:
                xor += "0"
            else:
                xor += "1"
    return xor


def xor_str(number1: str, number2: str):
    """
    Method use to perform the XOR operation between two integer given as string

    :param number1: The first number use to perform the XOR operation
    :type number1: str
    :param number2: The second number use to perform the XOR operation
    :type number2: str

    :return: The result of the XOR operation
    :rtype: str
    """
    xor = ""
    if len(number1) != len(number2):
        print("Error, the input must be the same size")
    for i in range(len(number1)):
        if number1[int(i)] == number2[int(i)]:
            xor += "0"
        else:
            xor += "1"
    return xor


def binaryDecimalAddition(binaryNumber, decimalAddition, lenthAlphabet, numberBits):
    """
    Method use to perform the addition between a binary number and a decimal number

    :param binaryNumber: The binary number use to perform the addition
    :type binaryNumber: str
    :param decimalAddition: The decimal number use to perform the addition
    :type decimalAddition: int
    :param lenthAlphabet: The lenth of the alphabet, in order to know which modulo to use
    :type lenthAlphabet: int
    :param numberBits: The number of bits use to represent the binary number
    :type numberBits: int

    :return: The result of the addition
    :rtype: str
    """
    decimalNumber = int(binaryNumber, 2)
    newNumber = (int(decimalNumber) + int(decimalAddition)) % lenthAlphabet
    newNumber = format(newNumber, 'b').zfill(int(numberBits))
    return newNumber