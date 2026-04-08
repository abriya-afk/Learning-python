"""
demonstrates string manipulation in Python, including concatenation, slicing, formatting and escape sequences.
"""
# String concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)   

# String slicing
sliced_greeting = full_greeting[0:5]
print(sliced_greeting)

# String formatting
formatted_greeting = f"{greeting}, {name}!"
print(formatted_greeting)

# Escape sequences
escaped_string = "This is a line with a newline character.\nAnd this is the next line."
print(escaped_string)