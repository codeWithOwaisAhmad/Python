"""
File Handling in Python
---------------------
Python provides built-in functions to Create, Read, Update, and Delete files.

Topics Covered:
1. File Modes (r, w, a, r+)
2. The 'with' statement Context Manager (Crucial Best Practice)
3. Reading/Writing Files (Text & JSON)
4. OS Module for File Deletion
"""

import os
import json

def basic_file_modes() -> None:
    """Understanding the modes."""
    print("--- 1. File Modes Primer ---")
    print("  'r' - Read (Default). Opens file for reading, errors if doesn't exist.")
    print("  'w' - Write. Opens file for writing, creates file if it doesn't exist, OVERWRITES content!")
    print("  'a' - Append. Opens file for appending, creates file if it doesn't exist.")
    print("  'b' - Binary mode (e.g., 'rb' or 'wb' for images/audio).")

def writing_and_appending() -> None:
    """Writing text to a file using best practices."""
    print("\n--- 2. Writing and Appending Files ---")
    
    filename = "demo.txt"
    
    # BAD PRACTICE:
    # f = open(filename, "w")
    # f.write("Hello")
    # f.close() # People often forget to close the file!
    
    # GOOD / PYTHONIC PRACTICE (Context Managers via 'with' keyword):
    print("Writing to file (truncating old content)...")
    with open(filename, "w") as file:
        file.write("Python File Handling is awesome!\n")
        file.writelines(["Line 2\n", "Line 3\n"])
        
    print("Appending to file (preserving old content)...")
    with open(filename, "a") as file:
        file.write("Appended Line 4\n")
        
    print("File write complete.")

def reading_files() -> None:
    """Reading from a file in various ways."""
    print("\n--- 3. Reading Files ---")
    
    filename = "demo.txt"
    try:
        with open(filename, "r") as file:
            print("Reading Entire File (.read()):")
            content = file.read()
            print(content)
            
            # Note: After .read(), the cursor is at EOF. Have to seek(0) to read again.
            file.seek(0)
            
            print("Reading line by line (Efficient for big files!):")
            for line in file:
                print(f" - {line.strip()}")
                
    except FileNotFoundError:
        print(f"Error: {filename} does not exist.")

def json_handling() -> None:
    """JSON reading and writing is arguably more common than plain text handling."""
    print("\n--- 4. Working with JSON Files (Interview Valid) ---")
    
    data_to_save = {
        "user_id": 101,
        "username": "Owais",
        "skills": ["Python", "Machine Learning", "Backend"]
    }
    
    json_filename = "data.json"
    
    # Save Dictionary to JSON String/File
    with open(json_filename, "w") as jf:
        json.dump(data_to_save, jf, indent=4)
    print(f"Saved JSON data to {json_filename}")
    
    # Read JSON File back to Dictionary
    with open(json_filename, "r") as jf:
        loaded_data = json.load(jf)
    print(f"Loaded JSON. Username: {loaded_data['username']}")

def cleanup_files() -> None:
    """Cleaning up the generated files."""
    print("\n--- 5. Deleting Files ---")
    if os.path.exists("demo.txt"):
        os.remove("demo.txt")
        print("Deleted demo.txt")
    if os.path.exists("data.json"):
        os.remove("data.json")
        print("Deleted data.json")

def interview_prep_gotchas() -> None:
    print("\n--- 6. Interview Prep & Gotchas ---")
    print("Question 1: Why should you ALWAYS use the 'with open()' statement and not just 'f = open()' ?")
    print("Answer: The 'with' statement is a Context Manager. It guarantees that the file handle ")
    print("is closed properly, even if an exception occurs halfway through reading/writing. ")
    print("Failing to close files leads to memory leaks and 'Too many open files' crashes.")

if __name__ == "__main__":
    print("🌟 Python File Handling 🌟")
    basic_file_modes()
    writing_and_appending()
    reading_files()
    json_handling()
    cleanup_files()
    interview_prep_gotchas()
