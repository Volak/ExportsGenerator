import pyperclip

def parse_string(input_string):
    # Extract the part after the third slash
    parts = input_string.split("/")
    if len(parts) <= 3:
        print("Invalid input. Ensure the string contains at least three slashes.")
        return None

    # Skip the first three segments (/All/ProjectName/)
    relevant_parts = parts[3:]  
    if not relevant_parts:
        print("No folders found to parse.")
        return None

    # Format the string with nested hierarchy
    output_lines = []
    for level, part in enumerate(relevant_parts):
        # Each part is indented based on its level
        output_lines.append(f"{'    ' * level}{part}<public> := module:")

    # Join lines with newlines to form the final output
    output = "\n".join(output_lines)
    return output

def main():
    while True:
        input_string = input("Enter your input string (e.g., /All/[Project Name]/Folder0/Folder1):\n")
        result = parse_string(input_string)
        if result:
            print("\nOutput:")
            print(result)
            # Copy to clipboard
            pyperclip.copy(result)
            print("\n(The result has been copied to your clipboard.)\n")

if __name__ == "__main__":
    main()
