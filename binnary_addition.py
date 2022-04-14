"""
Implement a function that adds two numbers together and returns their sum in binary.
The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))
"""


def add_binary(a, b):
    # return '1' if (a + b) == 1 else f'{(a + b):2b}'
    # return format(a + b, 'b')
    return '{0:b}'.format(a + b)
    # return bin(a + b)[2:]


print(add_binary(1,1))
