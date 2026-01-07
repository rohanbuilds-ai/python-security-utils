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
    print("File Reader")
    filename = input("Enter file name: ")

    try:
        lines, words = analyze_file(filename)
        print("\nFile Analysis:")
        print(f"Lines : {lines}")
        print(f"Words : {words}")
    except FileNotFoundError:
        print("Error: File not found.")


if __name__ == "__main__":
    main()
