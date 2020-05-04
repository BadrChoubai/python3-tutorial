# Hello, Python! - The Basics

## Python's Built-In Types

```python
# str() -> ''
# int() -> 0
# float() -> 0.0
# bool() -> False or True (0 or 1)
```

### Aside: Type Systems in Programming Languages

Programming languages can have either static types or dynamic types. Python is a dynamically typed language meaning that the type of a variable is allowed to change over time; `age = '22'` could later on become `age = 22`, it could also be changed to `age = False`.

## Variables

Variables in Python are nothing but reserved memory locations to store values.

```python
name = 'john doe' # str variable assignment
miles_travelled = 22.54 # = float variable assignment
meeting_in_session = True # bool variable assignment
```

## Functions

Functions are organized, reusable pieces of code that are used to perform a single, related action.

Functions in Python are denoted by the `def` keyword.

```python
def add(x, y):
    return x + y
```

*Easter Egg: The Zen of Python; Copy & Paste this in your terminal ```python3 -m this```*

---

## A Good First Program

[Starter File](hello.py)

Change the ouput of the `hello()` function so that it outputs `Hello, World!`

*To test your solution type `python3 test_hello.py` in your terminal*
