import argparse
from securepass.generator import generate_password
from securepass.entropy import calculate_entropy

def main():
    parser = argparse.ArgumentParser(
        description="SecurePass CLI password generator"
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

    args = parser.parse_args()

    password, charset_size = generate_password(args.length, args.symbols)
    entropy = calculate_entropy(charset_size, args.length)

    print("Password:", password)
    print(f"Entropy: {entropy:.2f} bits")

if __name__ == "__main__":
    main()

