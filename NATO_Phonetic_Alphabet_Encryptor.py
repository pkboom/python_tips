def encrypt_word(word):
    nato_alphabet = {
        "A": "Alfa",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliet",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "Xray",
        "Y": "Yankee",
        "Z": "Zulu",
    }

    encrypted_word = ""
    for letter in word:
        if letter.upper() in nato_alphabet:
            encrypted_word += nato_alphabet[letter.upper()] + " "
        else:
            encrypted_word += letter

    return encrypted_word


word = input("Enter a word: ")
encrypted_word = encrypt_word(word.strip())
print("Encrypted word: ", encrypted_word)
