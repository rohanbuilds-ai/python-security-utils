def parse_log_file(filename):
    """
    Parses a log file and counts:
    - total lines
    - error lines
    - warning lines
    Returns a tuple (total_lines, error_count, warning_count) 
    It handles file not found and permission errors.
    
    """
    total_lines = 0
    error_count = 0
    warning_count = 0

    try:
        with open(filename, "r") as file:
            for line in file:
                total_lines += 1
                line_lower = line.lower()

                if "error" in line_lower:
                    error_count += 1
                elif "warning" in line_lower:
                    warning_count += 1

        return total_lines, error_count, warning_count

    except FileNotFoundError:
        print("❌ Error: File not found.")
        return None
    except PermissionError:
        print("❌ Error: Permission denied.")
        return None


def main():
    print("Log File Analyzer")
    print("------------------")

    filename = input("Enter log file name: ").strip()

    result = parse_log_file(filename)

    if result:
        total, errors, warnings = result
        print("\nLog Summary")
        print(f"Total lines : {total}")
        print(f"Errors      : {errors}")
        print(f"Warnings    : {warnings}")
    else:
        print("Log analysis failed.")


if __name__ == "__main__":
    main()
