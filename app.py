"""
Random Password Generator
Generate strong and secure passwords with customizable length and character sets
"""

import random
import string


def get_password_length():
    """Get and validate password length from user"""
    while True:
        try:
            length = int(input("\nEnter password length (minimum 8): "))
            if length < 8:
                print("❌ Error: Password must be at least 8 characters long")
                continue
            if length > 128:
                print("⚠️  Warning: Password is very long. Continuing anyway...")
            return length
        except ValueError:
            print("❌ Error: Please enter a valid number")


def generate_password(length=12):
    """
    Generate a strong password with:
    - Uppercase letters
    - Lowercase letters
    - Digits
    - Special characters
    
    Args:
        length (int): Desired password length
        
    Returns:
        str: Generated password
    """
    
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure at least one character from each set
    password_chars = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill remaining length with random characters from all sets
    all_chars = uppercase + lowercase + digits + special
    for _ in range(length - 4):
        password_chars.append(random.choice(all_chars))
    
    # Shuffle to randomize positions
    random.shuffle(password_chars)
    
    # Join into password string
    password = ''.join(password_chars)
    
    return password


def check_password_strength(password):
    """
    Analyze password strength
    
    Args:
        password (str): Password to check
        
    Returns:
        str: Strength level
    """
    strength = 0
    
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1
    
    strength_levels = {
        1: "🔴 Weak",
        2: "🟡 Fair",
        3: "🟢 Good",
        4: "💪 Very Strong"
    }
    
    return strength_levels.get(strength, "🔴 Weak")


def main():
    """Main password generator loop"""
    print("=" * 55)
    print("🔐 Secure Password Generator")
    print("=" * 55)
    print("\n✅ Features:")
    print("   • Uppercase letters (A-Z)")
    print("   • Lowercase letters (a-z)")
    print("   • Digits (0-9)")
    print("   • Special characters (!@#$...)")
    
    while True:
        # Get password length
        length = get_password_length()
        
        # Generate password
        password = generate_password(length)
        
        # Check strength
        strength = check_password_strength(password)
        
        # Display password
        print(f"\n{'='*55}")
        print(f"🎉 Generated Password: {password}")
        print(f"📊 Strength: {strength}")
        print(f"📏 Length: {len(password)} characters")
        print(f"{'='*55}")
        
        # Copy suggestion
        print("\n💡 Copy password above (safe in clipboard)")
        
        # Ask to generate another
        while True:
            choice = input("\nGenerate another password? (yes/no): ").strip().lower()
            if choice in ['yes', 'y', 'ha', 'h']:
                break
            elif choice in ['no', 'n', 'yo\'q']:
                print("\n👋 Thank you for using Password Generator!")
                print("🔒 Remember to store passwords securely!")
                return
            else:
                print("❌ Please enter 'yes' or 'no'")


if __name__ == "__main__":
    main()
