FILENAME = "notes.txt"

def write_note():
    note = input("Enter a short note: ").strip()
    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            f.write(note + "\n")
        print("Saved note to", FILENAME)
    except Exception as e:
        print("Could not save note:", e)

def read_file():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            content = f.read()
        print("\nFile content:")
        print("----------------")
        print(content if content else "(file is empty)")
        print("----------------\n")
    except FileNotFoundError:
        print("File not found. Run the write step first.")
    except Exception as e:
        print("Could not read file:", e)

def append_note():
    note = input("Enter another note to append: ").strip()
    try:
        with open(FILENAME, "a", encoding="utf-8") as f:
            f.write(note + "\n")
        print("Appended note to", FILENAME)
    except Exception as e:
        print("Could not append note:", e)

def main():
    print("Step 1 write a note")
    write_note()

    print("Step 2 read the file")
    read_file()

    print("Step 3 append a new note")
    append_note()

    print("Step 4 read updated file")
    read_file()

if __name__ == "__main__":
    main()