import string
alphabet = string.ascii_lowercase

def encrypt(text, key):
    text = str(text).lower().translate(None, string.punctuation).replace(" ", "")
    key = str(key).lower().translate(None, string.punctuation).replace(" ", "")
    key = (key + text)[0:len(text)]
    output = ""
    for i in range(0,len(text)):
        x = alphabet.find(key[i])
        shifted_alphabet = alphabet[x:] + alphabet[:x]
        table = string.maketrans(alphabet, shifted_alphabet)
        output += text[i].translate(table)
    return output.upper()

def decrypt(text, key):
    text = str(text).lower().translate(None, string.punctuation).replace(" ", "")
    key = str(key).lower().translate(None, string.punctuation).replace(" ", "")
    output = ""
    for i in range(0,len(key)):
        x = alphabet.find(key[i])
        shifted_alphabet = alphabet[-x:] + alphabet[:-x]
        table = string.maketrans(alphabet, shifted_alphabet)
        output += text[i].translate(table)
    for i in range(0, len(text)-len(key)):
        x = alphabet.find(output[i])
        shifted_alphabet = alphabet[-x:] + alphabet[:-x]
        table = string.maketrans(alphabet, shifted_alphabet)
        output += text[i + len(key)].translate(table)
    return output.lower()

while True:
    print("1 - Encrypt")
    print("2 - Decrypt")
    command = int(input("Please select option number: "))
    if command == 1:
        plaintext = str(open("plaintext.txt", "r").readlines())[2:-2]
        key = str(open("key.txt", "r").readlines())[2:-2]
        print("Plaintext: %s" %plaintext)
        print("Encryption Key: %s" %key)
        print("Ciphertext: %s" %encrypt(plaintext, key))
        write = input("Write to ciphertext.txt (1-yes / 0-no)? ")
        if write == 1:
            ciphertext_file = open("ciphertext.txt", "w")
            ciphertext_file.write(encrypt(plaintext, key))
            ciphertext_file.close()
        break
    elif command == 2:
        ciphertext = str(open("ciphertext.txt", "r").readlines())[2:-2].replace(" ", "")
        key = str(open("key.txt", "r").readlines())[2:-2]
        print("Ciphertext: %s" %ciphertext)
        print("Decryption Key: %s" %key)
        print("Plaintext: %s" %decrypt(ciphertext,key))
        break