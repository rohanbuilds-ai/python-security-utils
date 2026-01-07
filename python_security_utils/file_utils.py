def read_file_stats(filename):
    line_count = 0
    word_count = 0

    with open(filename, "r") as file:
        for line in file:
            line_count += 1
            word_count += len(line.split())

    return line_count, word_count

def analyze_file(filename):
    """
    Reads a text file and counts
    lines and words.
    """
    line_count = 0
    word_count = 0

    with open(filename, "r") as file:
        for line in file:
            line_count += 1
            words = line.split()
            word_count += len(words)

    return line_count, word_count


def main():
    print("Safe File Reader")
    filename = input("Enter file name: ").strip()

    try:
        lines, words = read_file_stats(filename)

        print("\nFile Statistics")
        print(f"Lines : {lines}")
        print(f"Words : {words}")

    except FileNotFoundError:
        print("❌ Error: File not found.")
    except PermissionError:
        print("❌ Error: Permission denied.")


if __name__ == "__main__":
    main()
