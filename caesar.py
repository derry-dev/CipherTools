import string
alphabet = string.ascii_lowercase

def encrypt(text, x): #Shifts alphabet at position x
    text = str(text).lower().translate(None, string.punctuation).replace(" ", "")
    shifted_alphabet = alphabet[x:] + alphabet[:x]
    print (shifted_alphabet)
    table = string.maketrans(alphabet, shifted_alphabet)
    return text.translate(table).upper()

def decrypt(text, x): #Shifts alphabet at position 26-x
    text = str(text).lower().translate(None, string.punctuation).replace(" ", "")
    shifted_alphabet = alphabet[-x:] + alphabet[:-x]
    table = string.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

while True:
    print("1 - Encrypt")
    print("2 - Decrypt")
    command = int(input("Please select option number: "))
    if command == 1:
        plaintext = str(open("plaintext.txt", "r").readlines())[2:-2]
        shift = int(input("Please specify positions to shift (1 to 25): "))
        print("Plaintext: %s" %plaintext)
        print("Ciphertext: %s" %encrypt(plaintext,shift))
        write = input("Write to ciphertext.txt (1-yes / 0-no)? ")
        if write == 1:
            ciphertext_file = open("ciphertext.txt", "w")
            ciphertext_file.write(encrypt(plaintext,shift))
            ciphertext_file.close()
        break
    elif command == 2:
        ciphertext = str(open("ciphertext.txt", "r").readlines())[2:-2]
        print("Ciphertext: %s" %ciphertext)
        print("Possible plaintexts:")
        for i in range(1,26):
            print("%s. %s" %(i, decrypt(ciphertext,i)))
        break