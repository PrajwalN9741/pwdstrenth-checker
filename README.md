
# Password Strength Checker 🔐

This project is a simple C-based tool designed to evaluate the strength of user-entered passwords. It analyzes various characteristics of the password and provides feedback indicating whether it is Weak, Moderate, or Strong.

---

## 🚀 Features

- Evaluates password strength based on:
  - Password length
  - Use of uppercase and lowercase letters
  - Presence of numbers
  - Inclusion of special characters
- Categorizes password as:
  - Weak
  - Moderate
  - Strong
- Easy to compile and run on Linux systems

---

## 🧑‍💻 Getting Started

### 🔧 Prerequisites

- GCC (GNU Compiler Collection)
- Git (for cloning the repository)

### 🐧 Installation on Linux

1. **Install Git (if not installed)**:
   ```bash
   sudo apt-get install git


2. **Clone the Repository**:

   ```bash
   git clone https://github.com/gasanthosh/Pass_strength_check.git
   cd Pass_strength_check
   ```

3. **Compile the Program**:

   ```bash
   gcc psc.c -o strength_checker
   ```

4. **Run the Program**:

   ```bash
   chmod +x strength_checker
   ./strength_checker
   ```


## 🧠 How It Works

* The program prompts the user to input a password.
* It then checks the password character by character to identify:

  * Lowercase and uppercase letters
  * Digits
  * Special symbols
* A score is assigned based on these characteristics.
* The final score determines the password strength and displays it to the user.

---

## 📋 Example Outputs

| Input            | Output               |
| ---------------- | -------------------- |
| `systemadmin`    | Password is Weak     |
| `systemADMIN`    | Password is Moderate |
| `admin@System_1` | Password is Strong   |

---

## 🔎 Notes

* Default compiled output file is `a.out` unless renamed.
* You can adjust the evaluation logic inside `psc.c` based on custom rules.
* This tool is ideal for beginners learning C and basic security practices.

---

## 👨‍🏫 Educational Use Only

This project is meant for educational and learning purposes. It is not intended for use in real-world security systems or applications.



---

Would you like a badge-based GitHub header, or conversion of this project to Python or web-based UI?
