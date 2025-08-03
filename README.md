
# 🔐 Password Strength Checker

A simple command-line tool to evaluate the strength of passwords based on various criteria such as length, use of uppercase/lowercase letters, digits, and special characters.

---

## 📋 Features

- Checks for:
  - ✅ Minimum length
  - ✅ Uppercase letters
  - ✅ Lowercase letters
  - ✅ Numbers
  - ✅ Special characters
- Rates the password as:
  - Very Weak
  - Weak
  - Moderate
  - Strong
  - Very Strong

---

## 🛠️ Requirements

- Python 3.x  
  *(No external libraries needed – uses built-in `re` module)*

---

## 💻 How to Run (Linux/macOS)

1. Clone the repository:
   ```bash
   git clone https://github.com/PrajwalN9741/pwdstrenth-checker.git
   cd pwdstrenth-checker


2. Run the Python script:

   ```bash
   python3 password_checker.py
   ```

---

## 🧪 Sample Output

```
Password: admin123
Password strength: Weak
```

```
Password: Admin@123
Password strength: Very Strong
```

---

## ✏️ Customization

If you want to test a custom password directly (without user input), edit the `main()` function in `password_checker.py` like this:

```python
def main():
    password = "YourPasswordHere"
    strength = check_password_strength(password)
    print(f"Password: {password}")
    print(f"Password strength: {strength}")
```


## 📚 Educational Use

This project is intended for learning and practicing Python, regular expressions, and basic security principles. Not recommended for use in production systems.




Let me know if you want me to push this directly to your repo as a pull request (or help you rename the repo to fix the typo: `pwdstrenth` → `pwdstrength`).

