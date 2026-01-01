import argparse
import secrets
import string
import math

def calculate_entropy(charset_size, length):
    # Entropy formula: log2(N^L) = L * log2(N)
    return length * math.log2(charset_size)

def generate_random_password(length, symbols):
    chars = string.ascii_letters + string.digits

    if symbols:
        chars += "!@#$%^&*()_+-=[]{}"

    password = "".join(secrets.choice(chars) for _ in range(length))
    entropy = calculate_entropy(len(chars), length)

    return password, entropy

def generate_wordlist_password(words, separator):
    password = separator.join(words)
    entropy = math.log2(len(words)) * len(words)
    return password, entropy

def main():
    parser = argparse.ArgumentParser(
        description="Secure CLI Password Generator"
    )

    parser.add_argument(
        "-l", "--length",
        type=int,
        default=16,
        help="Password length"
    )

    parser.add_argument(
        "-s", "--symbols",
        action="store_true",
        help="Include symbols"
    )

    parser.add_argument(
        "-w", "--words",
        nargs="+",
        help="Generate password from wordlist"
    )

    parser.add_argument(
        "--sep",
        default="-",
        help="Word separator"
    )

    args = parser.parse_args()

    if args.words:
        password, entropy = generate_wordlist_password(args.words, args.sep)
    else:
        password, entropy = generate_random_password(args.length, args.symbols)

    print("Password:", password)
    print(f"Entropy: {entropy:.2f} bits")

if __name__ == "__main__":
    main()

