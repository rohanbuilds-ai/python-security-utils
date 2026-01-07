def analyze_numbers(numbers):
    """
    Takes a list of numbers and returns
    minimum, maximum, and average.
    """
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return minimum, maximum, average


def main():
    print("Number Analyzer")
    print("Enter numbers separated by spaces:")

    user_input = input("> ")
    numbers = [float(num) for num in user_input.split()]

    min_val, max_val, avg_val = analyze_numbers(numbers)

    print("\nResults:")
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")
    print(f"Average : {avg_val}")


if __name__ == "__main__":
    main()