import random
import string

def generate_secure_password(length=12):
    """
    Generate a secure password based on the rules defined in rules.txt
    """
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Ensure at least one character from each required set
    password = [
        random.choice(lowercase),  # at least one lowercase
        random.choice(uppercase),  # at least one uppercase
        random.choice(digits),      # at least one digit
        random.choice(special)       # at least one special character
    ]
    
    # Combine all character sets for the rest of the password
    all_chars = lowercase + uppercase + digits + special
    
    # Fill the rest of the password length with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)

def check_password_strength(password):
    """
    Check if the generated password meets all rules
    """
    checks = {
        'length': len(password) >= 12,
        'uppercase': any(c.isupper() for c in password),
        'lowercase': any(c.islower() for c in password),
        'digit': any(c.isdigit() for c in password),
        'special': any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    }
    
    return all(checks.values()), checks

def main():
    """
    Main function to generate and display secure passwords
    """
    print("=" * 50)
    print("SECURE PASSWORD GENERATOR")
    print("=" * 50)
    print("\nGenerating password based on rules in rules.txt...\n")
    
    # Generate password
    password = generate_secure_password(14)  # 14 characters long
    
    # Verify it meets all rules
    is_strong, checks = check_password_strength(password)
    
    # Display the password
    print(f"Generated Password: {password}")
    print(f"Password Length: {len(password)}")
    print("\nPassword Composition Check:")
    print(f"✓ Length (12+): {'✓' if checks['length'] else '✗'}")
    print(f"✓ Uppercase: {'✓' if checks['uppercase'] else '✗'}")
    print(f"✓ Lowercase: {'✓' if checks['lowercase'] else '✗'}")
    print(f"✓ Digit: {'✓' if checks['digit'] else '✗'}")
    print(f"✓ Special Char: {'✓' if checks['special'] else '✗'}")
    
    if is_strong:
        print("\n✅ Password meets all security requirements!")
    else:
        print("\n⚠️  Password does not meet all requirements. Generating again...")
        main()  # Generate another password if this one isn't strong
    
    print("\n" + "=" * 50)

# Alternative version with more customization options
def generate_password_with_options(length=12, include_uppercase=True, 
                                   include_lowercase=True, include_digits=True, 
                                   include_special=True):
    """
    Generate a password with customizable options
    """
    chars = ""
    required_chars = []
    
    if include_uppercase:
        chars += string.ascii_uppercase
        required_chars.append(random.choice(string.ascii_uppercase))
    
    if include_lowercase:
        chars += string.ascii_lowercase
        required_chars.append(random.choice(string.ascii_lowercase))
    
    if include_digits:
        chars += string.digits
        required_chars.append(random.choice(string.digits))
    
    if include_special:
        special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        chars += special
        required_chars.append(random.choice(special))
    
    # Fill the rest of the password
    password = required_chars.copy()
    for _ in range(length - len(required_chars)):
        password.append(random.choice(chars))
    
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    # Run the main program
    main()
    
    # Uncomment the line below to generate multiple passwords at once
    # print("\nMultiple Password Examples:")
    # for i in range(5):
    #     print(f"Password {i+1}: {generate_secure_password(12)}")