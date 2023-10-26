def pofi(a):
    # Since i^1 = i and i^2 = -1, we can use the modulo operator to find the remainder
    # when a is divided by 4, and determine the result accordingly.
    remainder = a % 4
    
    if remainder == 0:
        return '1'
    elif remainder == 1:
        return 'i'
    elif remainder == 2:
        return '-1'
    else:
        return '-i'

# Example usage:
print(pofi(0))  # Output: '1'
print(pofi(1))  # Output: 'i'
print(pofi(2))  # Output: '-1'
print(pofi(3))  # Output: '-i'