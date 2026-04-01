"""
Regular Expressions (Regex) in Python
-----------------------------------
Regex is a powerful tool for searching, extracting, and manipulating 
string patterns. Python uses the built-in `re` module for regex.

Topics Covered:
1. re.search() vs re.match()
2. re.findall() vs re.finditer()
3. Substitution using re.sub()
4. Common Metacharacters
"""

import re

def regex_basics() -> None:
    """Basic pattern searching."""
    print("--- 1. re.search() vs re.match() ---")
    
    text: str = "The rain in Spain falls mainly on the plain."
    
    # re.search() scans through the string looking for the first location where the pattern matches
    search_result = re.search(r"Spain", text)
    if search_result:
        print(f"search('Spain'): Match found at index {search_result.start()} to {search_result.end()}")
    else:
        print("search('Spain'): No match")
        
    # re.match() ONLY checks for a match AT THE BEGINNING of the string.
    # Therefore, Spain won't match, but 'The' will.
    match_result = re.match(r"Spain", text)
    print(f"match('Spain'): Matches starting at index 0? -> {bool(match_result)}")
    
    match_result_2 = re.match(r"The", text)
    print(f"match('The'): Matches starting at index 0? -> {bool(match_result_2)}")

def findall_and_finditer() -> None:
    """Extracting all instances of a pattern."""
    print("\n--- 2. re.findall() vs re.finditer() ---")
    
    text: str = "Contact us at info@example.com or support@company.org. Don't email falsemail@!!!"
    
    # Basic Email Pattern
    # \w+    -> one or more alphanumeric characters
    # \.+    -> period (optional, handled differently here for simplicity, just \w+@\w+\.\w+)
    pattern = r"\w+@\w+\.\w+"
    
    print("Using re.findall(): Returns a list of strings")
    emails = re.findall(pattern, text)
    print(f"Emails found: {emails}")
    
    print("\nUsing re.finditer(): Returns an iterator of Match objects (giving index positions too)")
    for match in re.finditer(pattern, text):
        print(f"Found '{match.group()}' at {match.span()}")

def modification_and_groups() -> None:
    """Replacing text and extracting specific parts."""
    print("\n--- 3. Substitution & Groups ---")
    
    messy_text = "My     Python     Code   Is     Messy"
    
    # re.sub(pattern, replacement, string)
    # \s+ means ONE or MORE whitespace characters
    clean_text = re.sub(r"\s+", " ", messy_text)
    print(f"Original: '{messy_text}'")
    print(f"re.sub() cleaned: '{clean_text}'")
    
    # Capture Groups () allow extracting parts of a matched text
    log_line = "2026-04-01 INFO: System booted up normally"
    
    # Group 1: Date (YYYY-MM-DD), Group 2: Log Level
    log_pattern = r"^(\d{4}-\d{2}-\d{2}) ([A-Z]+): "
    
    match = re.search(log_pattern, log_line)
    if match:
        print(f"\nGroup 0 (Full Match): '{match.group(0)}'")
        print(f"Group 1 (Date Extract): '{match.group(1)}'")
        print(f"Group 2 (Level Extract): '{match.group(2)}'")

def interview_prep_gotchas() -> None:
    """Gotcha on Raw Strings."""
    print("\n--- 4. Interview Prep & Gotchas (Raw Strings) ---")
    
    print("Question 1: Why do Python Regex patterns always start with 'r', like r'\n'?")
    print("Answer: Raw Strings prefix ('r') tells Python not to process escape characters.")
    print("For example, '\\n' in a normal string is a NEWLINE. In a RAW string (r'\\n'), it is literally a backslash followed by 'n'.")
    print("Since Regex relies heavily on backslashes (\d for digits, \w for words), raw strings prevent Python from misinterpreting them before the Regex engine sees them.")

if __name__ == "__main__":
    print("🌟 Python Regular Expressions (re) 🌟")
    regex_basics()
    findall_and_finditer()
    modification_and_groups()
    interview_prep_gotchas()
