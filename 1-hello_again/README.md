# Hello World Two - tuple fu! 

## The Basics 2: Electric Boogaloo

### More Basic Types
```python
# str() -> ''
# int() -> 0
# float() -> 0.0
# bool -> True or False
```

### Basic Data Structures
```python
# list() -> []
# tuple() -> ()
```

lists and tuples act similarly in python except for one difference;
```python
my_tuple = ('foo', 'bar', 'baz')
my_list = ['foo', 'bar', 'baz']

my_list[0] = 'boo'
my_tuple[0] = 'boo' # This will throw an error

```

---

### A Good Second Program
[Starter File](wet_feet.py)

Write a function `mutate_tuple` that takes a `tuple` of `('foo', 'bar', 'baz')` and changes the first element of the tuple to `boo`

Make sure the function returns a tuple.