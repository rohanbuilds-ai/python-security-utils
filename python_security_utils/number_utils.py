def analyze_numbers(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average


def main():
    print("Safe Number Analyzer")
    print("Enter numbers separated by spaces:")

    user_input = input("> ").strip()

    try:
        numbers = [float(num) for num in user_input.split()]

        if not numbers:
            raise ValueError("No numbers provided")

        min_val, max_val, avg_val = analyze_numbers(numbers)

        print("\nResults")
        print(f"Minimum: {min_val}")
        print(f"Maximum: {max_val}")
        print(f"Average: {avg_val}")

    except ValueError:
        print("❌ Error: Please enter valid numbers only.")


if __name__ == "__main__":
    main()
