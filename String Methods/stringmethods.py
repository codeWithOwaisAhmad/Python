# string_methods_tutorial.py

"""
Python String Methods Tutorial
"""

# 1. capitalize()
print("1. capitalize()")
# Easy Example
text = "hello world"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: Hello world

# Medium Example
text = "123 hello world!"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: 123 hello world!

# Hard Example
text_list = ["hello world", "python programming", "capitalize method"]
capitalized_list = [text.capitalize() for text in text_list]
print(capitalized_list)  # Output: ['Hello world', 'Python programming', 'Capitalize method']

# 2. casefold()
print("\n2. casefold()")
# Easy Example
text = "Hello World"
casefolded_text = text.casefold()
print(casefolded_text)  # Output: hello world

# Medium Example
text1 = "Straße"
text2 = "strasse"
print(text1.casefold() == text2.casefold())  # Output: True

# Hard Example
text_list = ["Hello World", "Straße", "Python Programming"]
casefolded_list = [text.casefold() for text in text_list]
print(casefolded_list)  # Output: ['hello world', 'strasse', 'python programming']

# 3. center()
print("\n3. center()")
# Easy Example
text = "hello"
centered_text = text.center(10)
print(f"'{centered_text}'")  # Output: '  hello   '

# Medium Example
text = "hello"
centered_text = text.center(10, '-')
print(f"'{centered_text}'")  # Output: '--hello---'

# Hard Example
text_list = ["hello", "world", "python"]
centered_list = [text.center(10, '*') for text in text_list]
print(centered_list)  # Output: ['**hello***', '**world***', '**python**']

# 4. count()
print("\n4. count()")
# Easy Example
text = "hello world"
count = text.count('l')
print(count)  # Output: 3

# Medium Example
text = "hello world"
count = text.count('l', 0, 5)
print(count)  # Output: 2

# Hard Example
text_list = ["hello world", "python programming", "count method"]
count_list = [text.count('o') for text in text_list]
print(count_list)  # Output: [2, 2, 1]

# 5. encode()
print("\n5. encode()")
# Easy Example
text = "hello world"
encoded_text = text.encode()
print(encoded_text)  # Output: b'hello world'

# Medium Example
text = "hello world"
encoded_text = text.encode('utf-16')
print(encoded_text)  # Output: b'\xff\xfeh\x00e\x00l\x00l\x00o\x00 \x00w\x00o\x00r\x00l\x00d\x00'

# Hard Example
text_list = ["hello world", "python programming", "encode method"]
encoded_list = [text.encode('utf-8') for text in text_list]
print(encoded_list)  # Output: [b'hello world', b'python programming', b'encode method']

# 6. endswith()
print("\n6. endswith()")
# Easy Example
text = "hello world"
ends_with = text.endswith('world')
print(ends_with)  # Output: True

# Medium Example
text = "hello world"
ends_with = text.endswith('hello', 0, 5)
print(ends_with)  # Output: True

# Hard Example
text_list = ["hello world", "python programming", "endswith method"]
ends_with_list = [text.endswith('ing') for text in text_list]
print(ends_with_list)  # Output: [False, True, False]

# 7. expandtabs()
print("\n7. expandtabs()")
# Easy Example
text = "hello\tworld"
expanded_text = text.expandtabs()
print(expanded_text)  # Output: hello   world

# Medium Example
text = "hello\tworld"
expanded_text = text.expandtabs(4)
print(expanded_text)  # Output: hello   world

# Hard Example
text_list = ["hello\tworld", "python\tprogramming", "expandtabs\tmethod"]
expanded_list = [text.expandtabs(8) for text in text_list]
print(expanded_list)  # Output: ['hello   world', 'python  programming', 'expandtabs       method']

# 8. find()
print("\n8. find()")
# Easy Example
text = "hello world"
index = text.find('world')
print(index)  # Output: 6

# Medium Example
text = "hello world"
index = text.find('o', 5)
print(index)  # Output: 7

# Hard Example
text_list = ["hello world", "python programming", "find method"]
index_list = [text.find('o') for text in text_list]
print(index_list)  # Output: [4, 4, -1]

# 9. format()
print("\n9. format()")
# Easy Example
text = "Hello, {}!".format('world')
print(text)  # Output: Hello, world!

# Medium Example
text = "Hello, {name}!".format(name='world')
print(text)  # Output: Hello, world!

# Hard Example
text_list = ["Hello, {0}!", "Welcome to {0}", "This is {0} method"]
formatted_list = [text.format('format') for text in text_list]
print(formatted_list)  # Output: ['Hello, format!', 'Welcome to format', 'This is format method']

# 10. format_map()
print("\n10. format_map()")
# Easy Example
text = "Hello, {name}!"
formatted_text = text.format_map({'name': 'world'})
print(formatted_text)  # Output: Hello, world!

# Medium Example
class Default(dict):
    def __missing__(self, key):
        return key

text = "Hello, {name}!"
formatted_text = text.format_map(Default(name='world'))
print(formatted_text)  # Output: Hello, world!

# Hard Example
text_list = ["Hello, {name}!", "Welcome to {place}", "This is {method} method"]
formatted_list = [text.format_map(Default(name='world', place='Python', method='format_map')) for text in text_list]
print(formatted_list)  # Output: ['Hello, world!', 'Welcome to Python', 'This is format_map method']

# 11. index()
print("\n11. index()")
# Easy Example
text = "hello world"
index = text.index('world')
print(index)  # Output: 6

# Medium Example
text = "hello world"
index = text.index('o', 5)
print(index)  # Output: 7

# Hard Example
text_list = ["hello world", "python programming", "index method"]
index_list = [text.index('o') for text in text_list if 'o' in text]
print(index_list)  # Output: [4, 4]

# 12. isalnum()
print("\n12. isalnum()")
# Easy Example
text = "hello123"
is_alnum = text.isalnum()
print(is_alnum)  # Output: True

# Medium Example
text = "hello 123"
is_alnum = text.isalnum()
print(is_alnum)  # Output: False

# Hard Example
text_list = ["hello123", "python programming", "isalnummethod"]
is_alnum_list = [text.isalnum() for text in text_list]
print(is_alnum_list)  # Output: [True, False, True]

# 13. isalpha()
print("\n13. isalpha()")
# Easy Example
text = "hello"
is_alpha = text.isalpha()
print(is_alpha)  # Output: True

# Medium Example
text = "hello123"
is_alpha = text.isalpha()
print(is_alpha)  # Output: False

# Hard Example
text_list = ["hello", "python123", "isalpha"]
is_alpha_list = [text.isalpha() for text in text_list]
print(is_alpha_list)  # Output: [True, False, True]

# 14. isascii()
print("\n14. isascii()")
# Easy Example
text = "hello"
is_ascii = text.isascii()
print(is_ascii)  # Output: True

# Medium Example
text = "hello©"
is_ascii = text.isascii()
print(is_ascii)  # Output: False

# Hard Example
text_list = ["hello", "python©", "isascii"]
is_ascii_list = [text.isascii() for text in text_list]
print(is_ascii_list)  # Output: [True, False, True]

# 15. isdecimal()
print("\n15. isdecimal()")
# Easy Example
text = "12345"
is_decimal = text.isdecimal()
print(is_decimal)  # Output: True

# Medium Example
text = "12345a"
is_decimal = text.isdecimal()
print(is_decimal)  # Output: False

# Hard Example
text_list = ["12345", "12345a", "isdecimal"]
is_decimal_list = [text.isdecimal() for text in text_list]
print(is_decimal_list)  # Output: [True, False, False]

# 16. isdigit()
print("\n16. isdigit()")
# Easy Example
text = "12345"
is_digit = text.isdigit()
print(is_digit)  # Output: True

# Medium Example
text = "12345a"
is_digit = text.isdigit()
print(is_digit)  # Output: False

# Hard Example
text_list = ["12345", "12345a", "isdigit"]
is_digit_list = [text.isdigit() for text in text_list]
print(is_digit_list)  # Output: [True, False, False]

# 17. isidentifier()
print("\n17. isidentifier()")
# Easy Example
text = "hello"
is_identifier = text.isidentifier()
print(is_identifier)  # Output: True

# Medium Example
text = "hello123"
is_identifier = text.isidentifier()
print(is_identifier)  # Output: True

# Hard Example
text_list = ["hello", "123hello", "isidentifier"]
is_identifier_list = [text.isidentifier() for text in text_list]
print(is_identifier_list)  # Output: [True, False, True]

# 18. islower()
print("\n18. islower()")
# Easy Example
text = "hello"
is_lower = text.islower()
print(is_lower)  # Output: True

# Medium Example
text = "Hello"
is_lower = text.islower()
print(is_lower)  # Output: False

# Hard Example
text_list = ["hello", "Hello", "islower"]
is_lower_list = [text.islower() for text in text_list]
print(is_lower_list)  # Output: [True, False, True]

# 19. isnumeric()
print("\n19. isnumeric()")
# Easy Example
text = "12345"
is_numeric = text.isnumeric()
print(is_numeric)  # Output: True

# Medium Example
text = "12345a"
is_numeric = text.isnumeric()
print(is_numeric)  # Output: False

# Hard Example
text_list = ["12345", "12345a", "isnumeric"]
is_numeric_list = [text.isnumeric() for text in text_list]
print(is_numeric_list)  # Output: [True, False, False]

# 20. isprintable()
print("\n20. isprintable()")
# Easy Example
text = "hello"
is_printable = text.isprintable()
print(is_printable)  # Output: True

# Medium Example
text = "hello\n"
is_printable = text.isprintable()
print(is_printable)  # Output: False

# Hard Example
text_list = ["hello", "hello\n", "isprintable"]
is_printable_list = [text.isprintable() for text in text_list]
print(is_printable_list)  # Output: [True, False, True]

# 21. isspace()
print("\n21. isspace()")
# Easy Example
text = " "
is_space = text.isspace()
print(is_space)  # Output: True

# Medium Example
text = "hello "
is_space = text.isspace()
print(is_space)  # Output: False

# Hard Example
text_list = [" ", "hello ", "isspace"]
is_space_list = [text.isspace() for text in text_list]
print(is_space_list)  # Output: [True, False, False]

# 22. istitle()
print("\n22. istitle()")
# Easy Example
text = "Hello World"
is_title = text.istitle()
print(is_title)  # Output: True

# Medium Example
text = "Hello world"
is_title = text.istitle()
print(is_title)  # Output: False

# Hard Example
text_list = ["Hello World", "Hello world", "istitle Method"]
is_title_list = [text.istitle() for text in text_list]
print(is_title_list)  # Output: [True, False, True]

# 23. isupper()
print("\n23. isupper()")
# Easy Example
text = "HELLO"
is_upper = text.isupper()
print(is_upper)  # Output: True

# Medium Example
text = "Hello"
is_upper = text.isupper()
print(is_upper)  # Output: False

# Hard Example
text_list = ["HELLO", "Hello", "ISUPPER"]
is_upper_list = [text.isupper() for text in text_list]
print(is_upper_list)  # Output: [True, False, True]

# 24. join()
print("\n24. join()")
# Easy Example
text = "hello"
joined_text = "-".join(text)
print(joined_text)  # Output: h-e-l-l-o

# Medium Example
words = ["hello", "world"]
joined_text = " ".join(words)
print(joined_text)  # Output: hello world

# Hard Example
text_list = ["hello", "world", "join method"]
joined_list = ["-".join(text) for text in text_list]
print(joined_list)  # Output: ['h-e-l-l-o', 'w-o-r-l-d', 'j-o-i-n- -m-e-t-h-o-d']

# 25. ljust()
print("\n25. ljust()")
# Easy Example
text = "hello"
ljust_text = text.ljust(10)
print(f"'{ljust_text}'")  # Output: 'hello     '

# Medium Example
text = "hello"
ljust_text = text.ljust(10, '-')
print(f"'{ljust_text}'")  # Output: 'hello-----'

# Hard Example
text_list = ["hello", "world", "ljust"]
ljust_list = [text.ljust(10, '*') for text in text_list]
print(ljust_list)  # Output: ['hello*****', 'world*****', 'ljust*****']

# 26. lower()
print("\n26. lower()")
# Easy Example
text = "HELLO"
lower_text = text.lower()
print(lower_text)  # Output: hello

# Medium Example
text = "HeLLo WoRLD"
lower_text = text.lower()
print(lower_text)  # Output: hello world

# Hard Example
text_list = ["HELLO", "WORLD", "LOWER"]
lower_list = [text.lower() for text in text_list]
print(lower_list)  # Output: ['hello', 'world', 'lower']

# 27. lstrip()
print("\n27. lstrip()")
# Easy Example
text = "   hello"
lstrip_text = text.lstrip()
print(f"'{lstrip_text}'")  # Output: 'hello'

# Medium Example
text = "---hello"
lstrip_text = text.lstrip('-')
print(f"'{lstrip_text}'")  # Output: 'hello'

# Hard Example
text_list = ["   hello", "---world", "###lstrip"]
lstrip_list = [text.lstrip(' -#') for text in text_list]
print(lstrip_list)  # Output: ['hello', 'world', 'lstrip']

# 28. maketrans() and translate()
print("\n28. maketrans() and translate()")
# Easy Example
text = "hello"
trans_table = text.maketrans("h", "y")
translated_text = text.translate(trans_table)
print(translated_text)  # Output: yello

# Medium Example
text = "hello world"
trans_table = text.maketrans("hw", "yz")
translated_text = text.translate(trans_table)
print(translated_text)  # Output: yello zorld

# Hard Example
text_list = ["hello", "world", "maketrans"]
translated_list = [text.translate(text.maketrans("aeiou", "12345")) for text in text_list]
print(translated_list)  # Output: ['h2ll4', 'w4rld', 'm1k2tr1ns']

# 29. partition()
print("\n29. partition()")
# Easy Example
text = "hello world"
partitioned_text = text.partition(" ")
print(partitioned_text)  # Output: ('hello', ' ', 'world')

# Medium Example
text = "hello world"
partitioned_text = text.partition("o")
print(partitioned_text)  # Output: ('hell', 'o', ' world')

# Hard Example
text_list = ["hello world", "python programming", "partition method"]
partitioned_list = [text.partition(" ") for text in text_list]
print(partitioned_list)  # Output: [('hello', ' ', 'world'), ('python', ' ', 'programming'), ('partition', ' ', 'method')]

# 30. replace()
print("\n30. replace()")
# Easy Example
text = "hello world"
replaced_text = text.replace("world", "Python")
print(replaced_text)  # Output: hello Python

# Medium Example
text = "hello world world"
replaced_text = text.replace("world", "Python", 1)
print(replaced_text)  # Output: hello Python world

# Hard Example
text_list = ["hello world", "world of Python", "replace method"]
replaced_list = text.replace("world", "universe")
print(replaced_list) 