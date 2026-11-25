print("hello")
Name= input("enter your name:")

# "a" opens the file in append mode so existing data isn't erased
with open("data.txt", "a", encoding="utf-8") as file:
    file.write(Name + "\n")

print("Saved!")
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        # Read the entire file at once
        content = file.read()
        print("--- Saved Data ---")
        print(content)
except FileNotFoundError:
    print("No data file found yet.")
    delete = input("Enter the exact text to delete: ")

target = input("Enter the exact text to delete: ")

try:
    # 1. Read all existing lines
    with open("data.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    # 2. Keep only the lines that do not match the user's input
    updated_lines = [line for line in lines if line.strip() != target]

    # 3. Overwrite the file ("w") with the remaining lines
    if x==("916"):
        while(updated_lines) < (lines):
        with open("data.txt", "w", encoding="utf-8") as file:
            file.writelines(updated_lines)
        print("Deleted successfully!")
    else:
        print("Item not found.")

except FileNotFoundError:
    print("No data file found yet.")

