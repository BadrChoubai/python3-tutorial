# Lists and Tuples in Python

In this lesson, we cover the basics of both lists and tuples.

## Lists

```python
# list syntax = []
cities = ['Pueblo', 'Denver', 'Centennial', 'Sterling']
```

## Tuples

```python
# tuple syntax = ()
cars = (('Subaru', ['forester', 'legacy']), ('Honda', ['accord', 'civic']))
```

### Mutability and Immutability in Python

[Reference](https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747)

In programming, there is the concept of immutable and mutable objects. In object-oriented programming an object is typically expressed as immutable to improve readability and runtime efficiency.

If an object is immutable, it means that we **cannot** modify it's state after it is created.

If an object is mutable, it means that we **can** modify it's state after it is created.

- Immutable object types in Python
  - `int`
  - `float`
  - `str`
  - `tuple`
  - frozen `set` [immutable version of set]

- Mutable object types in Python
  - `list`
  - `dict`
  - `set`
  - `byte` array

## Python `isinstance()` Method

The `isinstance()` method in Python allows you to check whether the object (first value), is an instance of classinfo class (second argument), Returning a boolean value if True.

### Usage

```python
cities = ['Lakewood', 'Golden', 'Ft. Collins']
print(isinstance(cities, list))
# >>> True
```

## Practice

Fill out the `mutate_tuple` function so that it returns `items` with `items[index]` being equal to `value`.

*To test your solution type `python3 test_mutate_tuple.py` in your terminal*
