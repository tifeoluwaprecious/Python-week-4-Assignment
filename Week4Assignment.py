
# File Read & Write Challenge

try:
    # Read from input.txt
    with open("input.txt", "r") as infile:
        content = infile.read()

    # Modify the content (convert to uppercase)
    modified_content = content.upper()

    # Write to output.txt
    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)

    print("Success! The modified text has been saved to output.txt")

except FileNotFoundError:
    print("Error: input.txt not found!")
except Exception as e:
    print(f"An error occurred: {e}")


# Error Handling Lab

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: You do not have permission to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
