# 🔐 Secure Password Generator

A Python-based password generator that creates strong, secure passwords with customizable length. Ensures inclusion of uppercase, lowercase, digits, and special characters.

## Features ✨

- **Strong Passwords**: Guarantees uppercase, lowercase, digits, and special characters
- **Customizable Length**: Minimum 8 characters, no maximum limit
- **Strength Indicator**: Visual feedback on password strength
- **Randomization**: Proper shuffling ensures maximum entropy
- **User-Friendly**: Clear prompts and error handling
- **Security Focused**: Uses Python's `random` and `string` modules
- **No Dependencies**: Works with standard library only

## Requirements 📋

- Python 3.6+
- No external dependencies

## Installation & Usage 🚀

### Run the generator:
```bash
python password_generator.py
```

### How to use:
1. Run the script
2. Enter desired password length (minimum 8 characters)
3. Get a randomly generated secure password
4. View password strength indicator
5. Choose to generate another or exit

### Example:
```
============================================================
🔐 Secure Password Generator
============================================================

✅ Features:
   • Uppercase letters (A-Z)
   • Lowercase letters (a-z)
   • Digits (0-9)
   • Special characters (!@#$...)

Enter password length (minimum 8): 16

============================================================
🎉 Generated Password: K7#mP2$vQx9!nL4@
📊 Strength: 💪 Very Strong
📏 Length: 16 characters
============================================================
```

## Code Structure 📁

```
02-password-generator/
├── password_generator.py  # Main application
└── README.md             # This file
```

## Functions 🔧

- `get_password_length()` - Get and validate length input from user
- `generate_password(length)` - Generate secure password with specified length
- `check_password_strength(password)` - Analyze and display password strength
- `main()` - Main generator loop

## Security Information 🔒

### Password Strength Levels:

- **🔴 Weak (1 type)**: Only one character type (bad)
- **🟡 Fair (2 types)**: Two character types (not recommended)
- **🟢 Good (3 types)**: Three character types (acceptable)
- **💪 Very Strong (4 types)**: All character types (recommended)

### Best Practices:

1. Minimum 8 characters for basic security
2. Use 12+ characters for important accounts
3. Use 16+ characters for highly sensitive accounts
4. Store passwords in a password manager
5. Never share passwords via email or unsecured channels

## Character Sets Used 🎨

```
Uppercase: A-Z (26 characters)
Lowercase: a-z (26 characters)
Digits:    0-9 (10 characters)
Special:   !@#$%^&*()_+-=[]{}|;:'",.<>?/ (32+ characters)
```

## Edge Cases Handled ⚠️

- ✅ Minimum length enforcement (8 characters)
- ✅ Invalid input handling
- ✅ Non-numeric input validation
- ✅ Very long passwords (up to 128+)

## Future Enhancements 💡

- Exclude ambiguous characters (0, O, l, 1, etc.)
- Custom character set selection
- Save generated passwords to encrypted file
- CLI flags for automation
- Password strength meter with tips

## Technical Details 🔧

### Randomization Method:

1. Create password array with one char from each set
2. Fill remaining slots with random chars from all sets combined
3. Shuffle array to randomize character positions
4. Join array into final password string

This ensures all character types are included while maintaining randomness.

## Common Issues 🐛

**Q: Password is too predictable?**
A: The shuffling algorithm randomizes positions. Each run produces different results.

**Q: Can I use very long passwords?**
A: Yes! No limit except system memory. 128+ characters supported.

**Q: How random is this?**
A: Uses Python's `random` module, suitable for most applications. For cryptographic security, use `secrets` module.

## Author 👨‍💻

Created as part of 1-week GitHub pushing marathon

## License 📜

MIT License - Free to use and modify
