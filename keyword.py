import string
alphabet = string.ascii_lowercase

def keygen(key):
    key = str(key).lower().translate(None, string.punctuation).replace(" ", "")
    stripped_alphabet = alphabet
    stripped_key = ""
    for i in range(0,len(key)):
        stripped_alphabet = stripped_alphabet.replace(key[i],"") 
        if key[i] not in stripped_key:
            stripped_key += key[i]
    return stripped_key + stripped_alphabet

def encrypt(text, key):
    text = str(text).lower().translate(None, string.punctuation).replace(" ", "")
    key = (keygen(key) * (len(text)/len(key) + 1))[0:len(text)]
    output = ""
    for i in range(0,len(text)):
        x = alphabet.find(key[i])
        shifted_alphabet = alphabet[x:] + alphabet[:x]
        table = string.maketrans(alphabet, shifted_alphabet)
        output += text[i].translate(table)
    return output.upper()

def decrypt(text, key):
    text = str(text).lower().translate(None, string.punctuation).replace(" ", "")
    key = (keygen(key) * (len(text)/len(key) + 1))[0:len(text)]
    output = ""
    for i in range(0,len(text)):
        x = alphabet.find(key[i])
        shifted_alphabet = alphabet[-x:] + alphabet[:-x]
        table = string.maketrans(alphabet, shifted_alphabet)
        output += text[i].translate(table)
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