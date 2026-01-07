def clean_string(text):
    """
    Cleans the input string by:
    - Removing extra spaces
    - Converting to lowercase
    - Counting characters
    """
    cleaned = text.strip().lower()
    char_count = len(cleaned)

    return cleaned, char_count


def main():
    print("String Cleaner")
    user_text = input("Enter a string: ")

    cleaned_text, length = clean_string(user_text)

    print("\nCleaned String:", cleaned_text)
    print("Character Count:", length)


if __name__ == "__main__":
    main()
