import argparse
import random
import string

def generate_password(length, use_symbols):
    chars = string.ascii_letters + string.digits

    if use_symbols:
        chars += "!@#$%^&*()_+-="

    password = ""
    for _ in range(length):
        password += random.choice(chars)

    return password

def main():
    parser = argparse.ArgumentParser(
        description="CLI Password Generator"
    )

    parser.add_argument(
        "-l", "--length",
        type=int,
        default=16,
        help="Length of password"
    )

    parser.add_argument(
        "-s", "--symbols",
        action="store_true",
        help="Include symbols"
    )

    args = parser.parse_args()

    pwd = generate_password(args.length, args.symbols)
    print("Generated password:", pwd)

if __name__ == "__main__":
    main()

