import string
alphabet = string.ascii_lowercase
reversed_alphabet = alphabet[::-1]

def encrypt(text):
    text = str(text).lower().translate(None, string.punctuation).replace(" ", "")
    table = string.maketrans(alphabet, reversed_alphabet)
    return text.translate(table).upper()

def decrypt(text):
    text = str(text).lower().translate(None, string.punctuation).replace(" ", "")
    table = string.maketrans(reversed_alphabet, alphabet)
    return text.translate(table)

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