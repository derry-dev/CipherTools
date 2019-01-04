import string
alphabet = string.ascii_lowercase
reversed_alphabet = alphabet[::-1]

def sort_ascending(data, array):
    for j in range(1,len(array)):
        key = array[j]
        temp = data[j]
        i = j - 1
        while i>=0 and array[i]>key:
            array[i+1] = array[i]
            data[i+1] =  data[i]
            i -= 1
        array[i+1] = key
        data[i+1] = temp
    return data

def sort_descending(data, array):
    for j in range(1,len(array)):
        key = array[j]
        temp = data[j]
        i = j - 1
        while i>=0 and array[i]<key:
            array[i+1] = array[i]
            data[i+1] =  data[i]
            i -= 1
        array[i+1] = key
        data[i+1] = temp
    print(array)
    return data

def encrypt(text, key):
    key = str(key).lower().translate(None, string.punctuation).replace(" ", "")
    i = 1
    while i < len(key): #removes duplicate letters
        if key[i] in key[:i]:
            key = key[:i] + key[i+1:]
        i += 1
    numbered_key = [0]*len(key)
    for i in range(len(key)): #converts key letters to alphabet position
        numbered_key[i] = alphabet.find(key[i])

    text = str(text).lower().translate(None, string.punctuation).replace(" ", "")
    columns = [""]*len(key)
    for i in range(len(text)):
        columns[i%len(key)] += text[i]

    columns = sort_ascending(columns,numbered_key)
    output = ""
    for i in range(len(text)):
        output += columns[i%len(columns)][0]
        columns[i%len(columns)] = columns[i%len(columns)][1:]
    return output.upper()

def decrypt(text, key):
    key = str(key).lower().translate(None, string.punctuation).replace(" ", "")
    i = 1
    while i < len(key):
        if key[i] in key[:i]:
            key = key[:i] + key[i+1:]
        i += 1
    numbered_key = [0]*len(key)
    for i in range(len(key)):
        numbered_key[i] = alphabet.find(key[i])
    print(numbered_key)
    numbered_key = sort_ascending(numbered_key,numbered_key) + [0]
    print(numbered_key)
    text = str(text).lower().translate(None, string.punctuation).replace(" ", "")
    columns = [""]*len(key)
    for i in range(len(text)):
        columns[i%len(columns)] += text[i]
    print(columns)
    columns = sort_descending(columns + ["placeholder"],numbered_key)
    print(columns)
    columns = columns[:-1]
    print(columns)
    output = ""
    for i in range(len(text)):
        output += columns[i%len(columns)][0]
        columns[i%len(columns)] = columns[i%len(columns)][1:]
    return output
  
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