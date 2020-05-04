# Python's Basic Types

## Numbers

There are three basic number types in Python but for the sake of this lesson we will focus on Integers and Floats.

Keep in Mind:

- Integers and floating points are separated by the presence or absence of a decimal point.  
- While integers can be of any length, a floating-point number is accurate only up to 15 decimal places (the 16th place is inaccurate).

### Numbers give you the ability to perform basic math in Python

```python
# Operators -> +, -, *, /, %, **
>>> 2 + 2
4
>>> 6 - 3
3

# Python will sometimes spit out an arbitrary number of decimal places
>>> 0.2 * 0.1
0.020000000000000004
>>> 4.0 / 2.0
2.0
>>> 4 % 2 # Modulo <-> Remainder
0

# Python supports order of operations
>>> (5 * 3) / 2
7.5
# and exponentiation using '**'
>>> 2**3
8

# Initializing a number variable
age = 21
pi = 3.14
```

## Strings

A string is simply a series of characters. Anything inside quotes is considered a string in Python.  

You can use single or double quotes around your strings like this:

```python
'Explicit is better than implicit.'
"Hiring? Check out my GitHub!"

# This flexibility lets you easily mix quotes and apostrophes.

'Nervously, a student asked "What is COBOL?".'

# Initializing a str() variable in python
street_name = 'Havana'

# You can use string concatenation to combine strings
first = 'john'
last = 'doe'
print(first+' '+last)
# >>> john doe
```

## Booleans

Booleans in programming are primarily used for control flow statements. In Python they are represented by the values `True` and `False`.

### Example in Code

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


is_even(4) # True
is_even(3) # False
```

## Python's `type()` method

The basic usage of the `type()` method in Python allows you to check the type of any object that is passed in.

### Usage

```python
full_name = "John Doe"

type(full_name) # <class 'str'>
type(3.14) # <class 'float'>
type(True) # <class 'bool'>
```
