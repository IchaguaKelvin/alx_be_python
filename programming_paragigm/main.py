import sys
from robust_division_calculator import safe_divide

def main():
    # Check if exactly two arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Get arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call safe_divide and print result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()