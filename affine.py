import string
alphabet = string.ascii_lowercase

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def modinverse(a,m):
    for i in range(1,m):
        if (m*i + 1) % a == 0:
            return (m*i + 1) // a
    return None

def encrypt(text, a, b):
    text = str(text).lower().translate(None, string.punctuation).replace(" ", "")
    output = ""
    for i in range(0,len(text)):
        output += alphabet[(a*alphabet.index(text[i])+b)%26]
    return output.upper()

def decrypt(text, a, b):
    text = str(text).lower().translate(None, string.punctuation).replace(" ", "")
    output = ""
    for i in range(0,len(text)):
        output += alphabet[(modinverse(a,26)*(alphabet.index(text[i])-b))%26]
    return output

while True:
    print("1 - Encrypt")
    print("2 - Decrypt")
    command = int(input("Please select option number: "))
    if command == 1:
        plaintext = str(open("plaintext.txt", "r").readlines())[2:-2]
        a = int(input("Input value for a: "))
        b = int(input("Input value for b: "))
        print("Plaintext: %s" %plaintext)
        print("Ciphertext: %s" %encrypt(plaintext,a,b))
        write = input("Write to ciphertext.txt (1-yes / 0-no)? ")
        if write == 1:
            ciphertext_file = open("ciphertext.txt", "w")
            ciphertext_file.write(encrypt(plaintext,a,b))
            ciphertext_file.close()
        break
    elif command == 2:
        ciphertext = str(open("ciphertext.txt", "r").readlines())[2:-2]
        print("Ciphertext: %s" %ciphertext)
        print("Possible plaintexts:")
        for i in range(2,26):
            for j in range(1,26):
                if modinverse(i,26) != None and (i*modinverse(i,26))%26 != 0:
                    print("a = %s, b = %s: %s" %(i, j, decrypt(ciphertext,i,j)))
        break