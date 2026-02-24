def evaluate_password(password):
    """
    Evaluate a password against security rules defined in B1 section
    Returns: (is_compliant, list_of_failed_rules)
    """
    failed_rules = []
    
    # Rule 1: Minimum length (at least 12 characters)
    if len(password) < 12:
        failed_rules.append("Password should have at least 12 characters")
    
    # Rule 2: Check for at least one uppercase letter
    if not any(c.isupper() for c in password):
        failed_rules.append("Password should contain at least one uppercase letter (A-Z)")
    
    # Rule 3: Check for at least one lowercase letter
    if not any(c.islower() for c in password):
        failed_rules.append("Password should contain at least one lowercase letter (a-z)")
    
    # Rule 4: Check for at least one digit
    if not any(c.isdigit() for c in password):
        failed_rules.append("Password should contain at least one digit (0-9)")
    
    # Rule 5: Check for at least one special character
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(c in special_chars for c in password):
        failed_rules.append("Password should contain at least one special character (!@#$%^&*()_+-=[]{}|;:,.<>?)")
    
    # Rule 6: Check for common patterns (sequential characters)
    sequential = False
    for i in range(len(password) - 2):
        # Check for sequential letters (abc, bcd, etc.)
        if (password[i].isalpha() and password[i+1].isalpha() and password[i+2].isalpha()):
            if (ord(password[i].lower()) + 1 == ord(password[i+1].lower()) and 
                ord(password[i+1].lower()) + 1 == ord(password[i+2].lower())):
                sequential = True
                break
        # Check for sequential numbers (123, 234, etc.)
        if (password[i].isdigit() and password[i+1].isdigit() and password[i+2].isdigit()):
            if (int(password[i]) + 1 == int(password[i+1]) and 
                int(password[i+1]) + 1 == int(password[i+2])):
                sequential = True
                break
    
    if sequential:
        failed_rules.append("Password should not contain sequential characters (e.g., abc, 123)")
    
    # Rule 7: Check for repeated characters
    repeated = False
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            repeated = True
            break
    
    if repeated:
        failed_rules.append("Password should not contain three or more repeated characters in a row")
    
    # Rule 8: Check for keyboard patterns (simplified check)
    keyboard_patterns = ['qwerty', 'asdfgh', 'zxcvbn', 'qwertz', 'azerty', 'qwertyuiop']
    password_lower = password.lower()
    for pattern in keyboard_patterns:
        if pattern in password_lower:
            failed_rules.append("Password should not contain keyboard patterns (e.g., qwerty, asdfgh)")
            break
    
    # Determine if compliant (no failed rules)
    is_compliant = len(failed_rules) == 0
    
    return is_compliant, failed_rules


def display_results(is_compliant, failed_rules):
    """
    Display the evaluation results in the required format
    """
    if is_compliant:
        print("\nCompliant.")
    else:
        print("\nNon-compliant.")
        print("The given password did not pass the following criteria:")
        for rule in failed_rules:
            print(f" - {rule}")


def main():
    """
    Main function to run the password evaluation program
    """
    print("=" * 60)
    print("PASSWORD STRENGTH EVALUATOR")
    print("=" * 60)
    
    # Ask for password input
    password = input("\nEnter the password string you want to evaluate: ")
    
    # Hide password input (optional - works in some terminals)
    # import getpass
    # password = getpass.getpass("Enter the password string you want to evaluate: ")
    
    # Evaluate the password
    print("\nEvaluating password against security rules...")
    is_compliant, failed_rules = evaluate_password(password)
    
    # Display results
    display_results(is_compliant, failed_rules)
    
    print("\n" + "=" * 60)


# Alternative simpler version with just the core 3 rules
def evaluate_password_simple(password):
    """
    Simpler evaluation with just 3 core rules
    """
    failed_rules = []
    
    # Rule 1: Minimum length
    if len(password) < 12:
        failed_rules.append("Password should have at least 12 characters")
    
    # Rule 2: Character diversity (at least one of each type)
    if not (any(c.isupper() for c in password) and 
            any(c.islower() for c in password) and 
            any(c.isdigit() for c in password) and 
            any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)):
        failed_rules.append("Password should contain at least one uppercase, one lowercase, one digit, and one special character")
    
    # Rule 3: No common patterns
    common_patterns = ['password', '123456', 'qwerty', 'abc123', 'admin', 'letmein']
    password_lower = password.lower()
    for pattern in common_patterns:
        if pattern in password_lower:
            failed_rules.append("Password should not contain common patterns or dictionary words")
            break
    
    is_compliant = len(failed_rules) == 0
    return is_compliant, failed_rules


if __name__ == "__main__":
    # Run the main program
    main()
    
    # Uncomment the line below to test with sample passwords
    # test_passwords()