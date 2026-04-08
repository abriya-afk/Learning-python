"""
Demonstrates arithmetic, comparison, logical, identity, membership, and bitwise operators.
"""


def show_operators():
    x = 10
    y = 3

    print("Arithmetic:", x + y, x - y, x * y, x / y, x // y, x % y, x**y)
    print("Comparison:", x > y, x == y, x != y)
    print("Logical:", (x > 5 and y < 5), (x < 5 or y < 5), not (x == y))

    nums = [1, 2, 3]
    print("Membership:", 2 in nums, 4 not in nums)

    a = nums
    b = [1, 2, 3]
    print("Identity:", a is nums, b is nums)

    print("Bitwise:", x & y, x | y, x ^ y, x << 1, x >> 1)
    
    print (id(b))
    print (id(nums))
    print (id(a))



show_operators()