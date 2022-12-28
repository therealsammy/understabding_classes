# Understanding Python First Class Functions, Closures, Classes, And Unit Tests

This module shows fundermental and intermediate concepts of the `Python` programming language. [^1]

The topics are:

- First class functions
- Closures
- Classes & Inheritance
- Unit Tests
- Doctess

## First Class Functions

A first-class function is not a particular kind of function. All functions in Python are first-class functions.

First-Class Functions are functions which are treated as so called "First-Class Citizens" (FCC). FCC's in a programming language are objects which:

    Can be used as parameters
    Can be used as a return value
    Can be assigned to variables
    Can be stored in data structures such as hash tables, lists, ...

Actually, very roughly and simply put, FCF's are variables of the type 'function' (or variables which point to a function). You can do with them everything you can do with a 'normal' variable.

```python
    def my_func(a, b):
        return a + b

    addition = my_func(2, 3)
    print(addition())
```

This is a simplistic example of first class functions.

> To say that functions are first-class in a certain programming language means that they can be passed around and manipulated similarly to how you would pass around and manipulate other kinds of objects (like integers or strings). You can assign a function to a variable, pass it as an argument to another function, etc. The distinction is not that individual functions can be first class or not, but that entire languages may treat functions as first-class objects, or may not. [BrenBran - StackOverflow](https://stackoverflow.com/a/27392443)

This is an extremely useful tool as they open the door to other topics dissused in this modules, like `closures`.

## Closures

[^1]: ~This module is a work in progress and new files will be added as this and directories will be added to this module.~
