
```md
# SecurePass CLI

SecurePass is a Python-based command-line password generator designed to demonstrate **progressive learning**, **secure randomness**, and **real-world password strength concepts**.

This repository contains multiple implementations of the same idea, ranging from beginner-level scripts to a properly packaged, security-focused CLI tool.

---

## Project Structure



securepass-cli/
├── scripts/                  # Learning and comparison versions
│   ├── password_easy.py
│   ├── password_medium.py
│   └── password_hard.py
│
├── securepass/               # Final packaged implementation
│   ├── **init**.py
│   ├── generator.py
│   ├── entropy.py
│   └── cli.py
│
├── pyproject.toml
├── README.md
└── LICENSE

````

---

## Project Levels Explained

### Easy Version (`scripts/password_easy.py`)

**Purpose**
- Learn basic Python syntax
- Understand how passwords are built from character sets

**Characteristics**
- Uses simple loops and string concatenation
- Uses the `random` module
- Takes user input via `input()`

**Limitations**
- Not cryptographically secure
- No CLI arguments
- No entropy calculation

This version exists purely for learning fundamentals.

---

### Medium Version (`scripts/password_medium.py`)

**Purpose**
- Transition from scripts to real CLI tools
- Improve structure and usability

**Characteristics**
- Uses `argparse`
- Supports configurable length and symbols
- Logic split into functions

**Limitations**
- Still uses the `random` module
- No entropy calculation
- Not suitable for real security use

This version focuses on practical scripting skills.

---

### Hard Version (Final Tool – `securepass/`)

**Purpose**
- Build a security-aware password generator
- Apply real-world password strength principles

**Characteristics**
- Uses `secrets` for cryptographically secure randomness
- Calculates entropy in bits
- Modular design (generator, entropy, CLI)
- Packaged as an installable CLI tool

This version represents the correct and secure implementation.

---

## How to Run the Code

### 1) Run Easy Version

```bash
python scripts/password_easy.py
````

You will be prompted for password length interactively.

---

### 2) Run Medium Version

```bash
python scripts/password_medium.py -l 20 -s
```

Options:

* `-l` set password length
* `-s` include symbols

---

### 3) Run Hard Version (Without Installing)

From the project root:

```bash
python -m securepass.cli -l 24 -s
```

---

### 4) Install and Use as a CLI Tool (Recommended)

```bash
pip install -e .
```

After installation:

```bash
securepass -l 24 -s
```

---

## Entropy Explained

Entropy measures the size of the password search space and estimates resistance to brute-force attacks.

Formula used:

```
Entropy = length × log2(character_set_size)
```

Higher entropy means:

* More possible combinations
* Higher computational cost for attackers

Entropy does not protect against phishing, keylogging, or password reuse.

---

## Security Notes

* Uses `secrets` instead of `random` for secure randomness
* Demonstrates why length is more important than symbols
* Intended for learning and demonstration
* Password storage and hashing are not implemented yet

---

## Future Improvements

* Crack-time estimation based on attacker models
* Wordlist-based passphrases in packaged version
* Password hashing using argon2id
* Unit tests
* PyPI publishing

---

