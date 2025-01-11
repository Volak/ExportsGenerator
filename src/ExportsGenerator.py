import pyperclip

def module_parse(input_string):
    """Parse input for Module Parse."""
    # Extract the part after the third slash
    parts = input_string.split("/")
    if len(parts) <= 3:
        print("Invalid input. Ensure the string contains at least three slashes.")
        return None

    relevant_parts = parts[3:]  # Skip the first three segments (e.g., /All/ProjectName/)
    if not relevant_parts:
        print("No folders found to parse.")
        return None

    # Format the string with nested hierarchy
    output_lines = []
    for level, part in enumerate(relevant_parts):
        output_lines.append(f"{'    ' * level}{part}<public> := module:")

    return "\n".join(output_lines)

def using_parse(input_string):
    """Parse input for Using Parse."""
    # Extract the part after the third slash
    parts = input_string.split("/")
    if len(parts) <= 3:
        print("Invalid input. Ensure the string contains at least three slashes.")
        return None

    relevant_parts = parts[3:]  # Skip the first three segments
    if not relevant_parts:
        print("No folders found to parse.")
        return None

    # Join parts with dots
    output = f"using {{ {'.'.join(relevant_parts)} }}"
    return output

def main():
    while True:
        # Show descriptions and options
        print("[1] Module Parse: Parses the directory path into a nested module format.")
        print("[2] Using Parse: Parses the directory path into a single 'using' statement.")
        choice = input("\nChoose an option: ")

        if choice not in ["1", "2"]:
            print("Invalid choice. Please select 1 or 2.\n")
            continue

        # Ask for the directory string
        input_string = input("\nEnter your directory path (e.g., /All/[Project Name]/Folder0/Folder1):\n")

        # Parse based on the chosen option
        if choice == "1":
            result = module_parse(input_string)
        elif choice == "2":
            result = using_parse(input_string)

        # Display and copy the result if valid
        if result:
            print("\nOutput:")
            print(result)
            pyperclip.copy(result)
            print("\n(The result has been copied to your clipboard.)\n\n")

        # Loop back to choose the next parse option

if __name__ == "__main__":
    main()
