def caesarCipherEncryptor(string, key):
    # Write your code here.
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(len(alphabet))
    new_word = []

    for letter in string:
        index = alphabet.index(letter) + key
        
        if index > 25:
            print(index % 26)
            new_word.append(alphabet[index % 26])
        else:
            new_word.append(alphabet[index])
    return "".join(new_word)


caesarCipherEncryptor("abc", 52)

