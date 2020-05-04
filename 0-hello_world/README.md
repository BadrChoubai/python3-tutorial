# Hello, Python! - The Basics

## Python's Four Basic Types

```python
# str() -> ''
# int() -> 0
# float() -> 0.0
# bool() -> False or True (0 or 1)
```

### Type Systems in Programming Languages

Programming languages can have either static types or dynamic types. Python is a dynamically typed language meaning that the type of a variable is allowed to change over time; `age = '22'` could later on become `age = 22`.

## Variables

Variables in Python are nothing but reserved memory locations to store values.

### Variable Naming Rules in Python

- Variable names must be a combination of letters (a-zA-Z), digits (0-9) or an underscore (_), and are case sensitive.
- A variable name cannot start with a number.
- [Reserved keywords in Python](https://www.programiz.com/python-programming/keyword-list) may not be used as variable names.
- Special characters are not allowed in variable names.

```python
person = 'john doe' # str variable assignment
miles_travelled = 22.54 # float variable assignment
meeting_in_session = True # bool variable assignment

# This is an invalid variable assignment
1nvalid = ''
# and so is this...
continue = True
```

## Functions

Functions are organized, reusable pieces of code that are used to perform a single, related action.

```python
# functions in Python are denoted by the `def` keyword.
def add(x, y):
    return x + y
```

*Easter Egg: The Zen of Python; Copy & Paste this in your terminal ```python3 -m this```*

---

## A Good First Program

[Starter File](hello.py)

Change the ouput of the `hello()` function so that it outputs `Hello, World!`

*To test your solution type `python3 test_hello.py` in your terminal*
