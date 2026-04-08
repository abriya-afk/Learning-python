"""
Demonstrates id() function and object identity.
"""


def show_identity():
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]

    print(f"id(a): {id(a)}")
    print(f"id(b): {id(b)}")
    print(f"id(c): {id(c)}")
    print(f"a is b? {a is b}")
    print(f"a is c? {a is c}")
    print(f"a == c? {a == c}")



show_identity()
