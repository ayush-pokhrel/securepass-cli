# securepass-cli
A Python CLI tool for generating secure passwords and passphrases with entropy analysis, demonstrating real-world password security concepts.

## Project Levels Explained (Easy → Medium → Hard)

This repository contains three versions of the same password generator project.
Each version represents a deliberate increase in complexity, security, and software engineering quality.

The goal is not just to generate passwords, but to understand **how and why secure password systems are built**.

---

### 1) Easy Version – Fundamentals

**Purpose**
- Learn basic Python syntax and control flow
- Understand how passwords are constructed from character sets

**Key Characteristics**
- Uses simple loops and string concatenation
- Generates passwords using letters, digits, and symbols
- Interactive input via `input()`

**Limitations**
- Uses the `random` module (not cryptographically secure)
- No command-line interface
- No entropy calculation
- Not suitable for real security use

**What This Level Teaches**
- How password generators work internally
- Why short or predictable passwords are weak
- Why “random-looking” does not automatically mean secure

This version is intentionally simple and educational.

---

### 2) Medium Version – Practical Scripting

**Purpose**
- Move from scripts to proper CLI tools
- Improve code structure and reusability

**Key Characteristics**
- Uses `argparse` for command-line arguments
- Optional symbol inclusion
- Logic separated into functions
- Default values for usability

**Improvements Over Easy**
- No interactive prompts, fully scriptable
- Cleaner and more maintainable code
- Usable in automation and shell workflows

**Limitations**
- Still uses the `random` module
- No entropy measurement
- Security is improved structurally, not cryptographically

**What This Level Teaches**
- How real command-line tools are built
- Why separation of logic matters
- How to design flexible interfaces

This version is a stepping stone from learning Python to writing usable tools.

---

### 3) Hard Version – Security-Focused Implementation

**Purpose**
- Build a security-aware password generator
- Understand real-world password strength and attack models

**Key Characteristics**
- Uses the `secrets` module for cryptographically secure randomness
- Calculates entropy in bits
- Supports wordlist-based passphrases
- Clear separation between generation logic and CLI

**Improvements Over Medium**
- Secure randomness suitable for password generation
- Entropy calculation based on search space math
- Demonstrates why length beats complexity
- More realistic and defensible security model

**What This Level Teaches**
- Why secure RNG matters
- How entropy quantifies brute-force resistance
- Why passphrases can be stronger than short complex passwords
- How security tools should be designed and reasoned about

This version is suitable for demonstration, learning, and further extension into hashing and storage.

---

### Overall Progression

- **Easy** focuses on understanding the problem
- **Medium** focuses on usability and structure
- **Hard** focuses on correctness, security, and real-world thinking

Each level builds directly on the previous one, reflecting a practical learning path rather than isolated scripts.
