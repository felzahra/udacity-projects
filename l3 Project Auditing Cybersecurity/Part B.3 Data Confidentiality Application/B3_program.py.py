def caesar_cipher(text, shift=3):
    """
    Encrypt text by shifting characters right by shift positions
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase separately
            if char.isupper():
                # Shift uppercase letters
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Shift lowercase letters
                shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += shifted
        else:
            # Keep non-alphabetic characters as is
            result += char
    return result

def caesar_decipher(text, shift=3):
    """
    Decrypt text by shifting characters left by shift positions
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase separately
            if char.isupper():
                # Shift uppercase letters back
                shifted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                # Shift lowercase letters back
                shifted = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            result += shifted
        else:
            # Keep non-alphabetic characters as is
            result += char
    return result

# Main program
def main():
    try:
        # Read from input.txt
        with open('input.txt', 'r') as file:
            plaintext = file.read()
        
        # Encrypt the text
        encrypted = caesar_cipher(plaintext)
        
        # Save encrypted text to encrypted.txt
        with open('encrypted.txt', 'w') as file:
            file.write(encrypted)
        
        # Decrypt the encrypted text
        decrypted = caesar_decipher(encrypted)
        
        # Save decrypted text to decrypted.txt
        with open('decrypted.txt', 'w') as file:
            file.write(decrypted)
        
        print("Process completed successfully!")
        print(f"Original text length: {len(plaintext)}")
        print(f"Encrypted text saved to encrypted.txt")
        print(f"Decrypted text saved to decrypted.txt")
        
    except FileNotFoundError:
        print("Error: input.txt file not found in the workspace.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()