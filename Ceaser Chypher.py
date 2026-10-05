# JA, CSP Ceaser Cypher

def caesar_shift(message, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    for char in message:
        if char in alphabet:
            old_pos = alphabet.find(char)
            new_pos = (old_pos + shift) % 26
            result += alphabet[new_pos]
        elif char in ALPHABET:
            old_pos = ALPHABET.find(char)
            new_pos = (old_pos + shift) % 26
            result += ALPHABET[new_pos]
        else:
            result += char
            
    return result

def main():
    choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ")
    message = input("Enter your message: ")
    shift = int(input("Enter a shift amount: "))
    
    if choice == "D" or choice == "d":
        shift = -shift
        
    output = caesar_shift(message, shift)
    
    if choice == "E" or choice == "e":
        print("Your encrypted message is:", output)
    else:
        print("Your decrypted message is:", output)

main()