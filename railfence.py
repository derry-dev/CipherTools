import string

def encrypt(text,rail):
    text = str(text).lower().translate(None, string.punctuation).replace(" ", "")
    fence = [""]*rail
    pos = ((list(range(0,rail)) + list(range(rail-2,0,-1)))*len(text))[0:len(text)]
    #pos gives the required sequence of rail numbers to append text
    for x in range(len(text)):
        fence[pos[x]] += (text[x])
    return string.join(fence,"").upper()

def decrypt(text,rail):
    text = str(text).lower().translate(None, string.punctuation).replace(" ", "")
    fence = [""]*rail
    pos = ((list(range(0,rail)) + list(range(rail-2,0,-1)))*len(text))[0:len(text)]
    for i in range(rail):
        fence[i] = text[0:pos.count(i)] + "0"
        text = text.replace(text[0:pos.count(i)],"")
    output = ""
    for i in pos:
        if fence[i] != "0":
            output += (fence[i])[0]
            fence[i] = fence[i][1:]
    return output

while True:
    print("1 - Encrypt")
    print("2 - Decrypt")
    command = int(input("Please select option number: "))
    if command == 1:
        plaintext = str(open("plaintext.txt", "r").readlines())[2:-2]
        rails = int(input("Please specify number of rails: "))
        print("Plaintext: %s" %plaintext)
        print("Ciphertext: %s" %encrypt(plaintext,rails))
        write = input("Write to ciphertext.txt (1-yes / 0-no)? ")
        if write == 1:
            ciphertext_file = open("ciphertext.txt", "w")
            ciphertext_file.write(encrypt(plaintext,rails))
            ciphertext_file.close()
        break
    elif command == 2:
        ciphertext = str(open("ciphertext.txt", "r").readlines())[2:-2]
        print("Ciphertext: %s" %ciphertext)
        print("Possible plaintexts:")
        for i in range(1,len(ciphertext)/2):
            print("%s. %s" %(i, decrypt(ciphertext,i)))
        break