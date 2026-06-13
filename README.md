# OIBSIP_PythonProgramming_Task3

# 🔐 Advanced Password Generator

A secure and user-friendly Password Generator built with Python and Tkinter. This application allows users to generate strong random passwords with customizable options such as letters, numbers, symbols, and exclusion of similar-looking characters.

## Features

. Generate secure random passwords

. Custom password length

. Include Letters (Uppercase & Lowercase)

. Include Numbers

. Include Symbols

. Exclude Similar Characters (O, 0, I, l, 1)

. Password Strength Indicator

. Copy Password to Clipboard

. Easy-to-use GUI with Tkinter

---

## Technologies Used

* Python 3
* Tkinter (GUI)
* Random Module
* String Module

---

## Project Structure

```python
generate_password()   # Generates secure passwords
copy_password()       # Copies password to clipboard

Tkinter GUI
├── Password Length Input
├── Character Type Selection
├── Generate Button
├── Password Display
├── Strength Indicator
└── Copy Button
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/echoesofnil/advanced-password-generator.git
cd advanced-password-generator
```

### Run the Application

```bash
python password_generator.py
```

---

## How It Works

1. Enter the desired password length.
2. Select character types:

   * Letters
   * Numbers
   * Symbols
3. Optionally exclude similar characters.
4. Click **Generate Password**.
5. View generated password and strength.
6. Copy password using the **Copy to Clipboard** button.

---

## Password Strength Rules

| Length             | Strength |
| ------------------ | -------- |
| 8 - 9 Characters   | Weak     |
| 10 - 13 Characters | Medium   |
| 14+ Characters     | Strong   |

---

## Example Output

```text
Password Length: 16

Generated Password:
K@8mT#4qP!2vX9&L

Password Strength:
Strong
```

---

## Security Features

* Ensures uppercase and lowercase letters when letters are selected.
* Ensures at least one number when numbers are selected.
* Ensures at least one symbol when symbols are selected.
* Prevents weak passwords below 8 characters.
* Option to remove confusing characters for better readability.

---

## Learning Outcomes

This project helped me learn:

* GUI Development with Tkinter
* Event Handling
* Password Security Principles
* Random Password Generation
* Clipboard Operations
* Input Validation
* Python Functions and Modules

---

## Future Improvements

* Dark Mode UI
* Password History
* Save Passwords Securely
* Password Entropy Calculation
* Password Expiry Suggestions
* Export Passwords to File
* Modern CustomTkinter Interface

---

## Author

Developed by Nilakshi 

A Python GUI project focused on cybersecurity fundamentals, password security, and desktop application development.
