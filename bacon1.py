import string
alphabet = "abcdefghiklmnopqrstvwxyz"
dictionary = []
for i in range(0,24):
    dictionary.append(("00000"+str((bin(i)[2:]))[0:6])[-5:])
    dictionary[i] = dictionary[i].replace("0","a").replace("1","b")

def encrypt(text):
    text = str(text).lower().translate(None, string.punctuation).replace(" ", "")
    text = text.replace("j","i").replace("u","v")
    output = ""
    for i in range(len(text)):
        output += dictionary[alphabet.index(text[i])]
    return output.upper()

def decrypt(text):
    text = str(text).lower().translate(None, string.punctuation).replace(" ", "")
    output = ""
    while len(text) > 0:
        output += alphabet[dictionary.index(text[0:5])]
        text = text[5:]
    return output

while True:
    print("1 - Encrypt")
    print("2 - Decrypt")
    command = int(input("Please select option number: "))
    if command == 1:
        plaintext = str(open("plaintext.txt", "r").readlines())[2:-2]
        print("Plaintext: %s" %plaintext)
        print("Ciphertext: %s" %encrypt(plaintext))
        write = input("Write to ciphertext.txt (1-yes / 0-no)? ")
        if write == 1:
            ciphertext_file = open("ciphertext.txt", "w")
            ciphertext_file.write(encrypt(plaintext))
            ciphertext_file.close()
        break
    elif command == 2:
        ciphertext = str(open("ciphertext.txt", "r").readlines())[2:-2]
        print("Ciphertext: %s" %ciphertext)
        print("Plaintext: %s" %decrypt(ciphertext))
        break