#Edward An

import string

def edit_cipher(cipher):
    '''This function removes duplicate characters in a cipher and converts uppercase to lowercase letters
    Input arguments: cipher must be a string
    Returns: An edited cipher without any duplicates or uppercase letters
    '''
    cipher_list = [] #Strings are immutable, so a list is created
    cipher = cipher.lower() #Capitals turn into lowercase
    for character in cipher: #Each character is put into a list only when it is unique.
        if character not in cipher_list:
            cipher_list.append(character)
    cipher = "".join(cipher_list) #List becomes a string. The duplicates are now removed and everything is lowercase
    return cipher

def is_cipher_valid(cipher):
    '''This function verifies whether a passed argument meets the criterias.
    The criterias are: 26 characters, no duplicate characters, only alphanumerics, and alphabets must all be lowercase.
    Input arguments: cipher must be a string
    Returns: True or False depending on the cipher's validity
    '''
    cipher_set = set(cipher)
    if ((len(cipher) == 26) and (len(cipher) == len(cipher_set)) and \
        (cipher.isalnum() == True) and (cipher.islower() == True)):#the criterias of a valid cipher are met
        print("You cipher is valid.")
        return True
    else: #the criterias of a valid cipher are not met
        print("Your cipher must contain 26 unique elements of a-z or 0-9.")
        return False

def assign_cipher_to_alphabet(cipher, translation_dictionary):
    '''This function iterates through all the keys of a translation dictionary using a for loop
    and assigns every character of a cipher into the corresponding value of the dictionary.
    This appends the dictionary to be in the form of [alphabet : cipher, ...]
    Input arguments: cipher must be a string, and translation_dictionary must be a dictionary.
    Returns: An appended dictionary.
    '''
    index = 0 #index of a string is set to zero
    for key in translation_dictionary:
        translation_dictionary[key] = cipher[index] #assignment of character into the value of the dictionary
        index = index + 1 #index increments up by 1
    return translation_dictionary

def encode(text_to_encode, translation_dictionary):
    '''This function turns a string into a list and runs a for loop "number of length of the text" times.
    In each iteration, the element in the list is replaced with the "value" aka cipher of the dictionary
    Input arguments: text_to_encode must be a string, and translation_dictionary must be a dictionary.
    Returns: Encoded text
    '''
    text_to_encode_list = list(text_to_encode) #Strings are immutable, so a list is created
    for index in range(len(text_to_encode_list)): #Repeats for all letters of the text
        char_in_text = text_to_encode_list[index]
        if char_in_text in translation_dictionary.keys():
            text_to_encode_list[index] = translation_dictionary[char_in_text]#Each character in the list is replaced with a value
    text_to_encode = "".join(text_to_encode_list) #List becomes a string
    return text_to_encode

def decode(text_to_decode, translation_dictionary):
    '''This function turns a string into a list and runs a for loop "number of length of the text" times.
    In each iteration, the element in the list is replaced with the "key" aka alphabet of the dictionary
    Input arguments: text_to_decode must be a string, and translation_dictionary must be a dictionary.
    Returns: Decoded text
    '''
    text_to_decode_list = list(text_to_decode) #Strings are immutable, so a list is created
    keys = list(translation_dictionary.keys()) 
    values = list(translation_dictionary.values())
    for index in range(len(text_to_decode_list)): #Repeats for all letters of the text
        char_in_text = text_to_decode_list[index]
        if char_in_text in translation_dictionary.values():
            text_to_decode_list[index] = keys[values.index(char_in_text)] #Each character in the list is replaced with a key
    text_to_decode = "".join(text_to_decode_list) #List becomes a string
    return text_to_decode



def main():
    #Dictionary that contains the alphabet as its key and the cipher as its value. By default there is no cipher.
    #The keys of the dictionary will never change, only the values will change.
    translation_dictionary = {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', 'f':'',\
                            'g':'', 'h':'', 'i':'', 'j':'', 'k':'', 'l':'', 'm':'',\
                            'n':'', 'o':'', 'p':'', 'q':'', 'r':'', 's':'','t':'',\
                            'u':'', 'v':'', 'w':'', 'x':'', 'y':'', 'z':''}

    repeat=True #This boolean variable allows the while loop to repeat. It is set to true by default.

    while (repeat == True):
        option = int(input("Select 1 to encode, select 2 to decode, or select 0 to end the program: "))

        if (option == 1): #User wants to encode a text
            text_to_encode = input("Please enter a text to be encoded: ")
            cipher = input("Please enter the cipher text: ")
            cipher = edit_cipher(cipher) #BONUS MARK FUNCTION CALL
            validity = is_cipher_valid(cipher) #cipher validity check
            if (validity == True):
                assign_cipher_to_alphabet(cipher, translation_dictionary)
                encrypted_message = encode(text_to_encode, translation_dictionary)
                print("Your output is:", encrypted_message)

        elif (option == 2): #User wants to decode a text
            text_to_decode = input("Please enter a text to be decoded: ")
            cipher = input("Please enter the cipher text: ")
            cipher = edit_cipher(cipher) #BONUS MARK FUNCTION CALL
            validity = is_cipher_valid(cipher) #cipher validity check
            if (validity == True):
                assign_cipher_to_alphabet(cipher, translation_dictionary)
                decrypted_message = decode(text_to_decode, translation_dictionary)
                print("Your output is:", decrypted_message)

        elif (option == 0): #User wants to end the program
            repeat = False

        else: #User enters any integer other than 0, 1, or 2
            print("Invalid entry. Please try again.")

    print("Goodbye")

#This code only runs as a script
if __name__ == '__main__':
    main()
