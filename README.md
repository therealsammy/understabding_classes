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

## [Closures]()

Like nested loops, we can also nest functions. That said, Python gives us the power to define functions within functions.

Python Closures are these inner functions that are enclosed within the outer function. Closures can access variables present in the outer function scope. It can access these variables even after the outer function has completed its execution.

```python
def outer_func(name):
    # this is the enclosing function

    def inner_func():
        # this is the enclosed function

        # the inner function accessing the outer function's variable 'name'
        print(name)

    inner_func()

# call the enclosing function
outer('Sam')
```

**Output**

        Sam

Let’s break this code down.

When the outer function gets called, the variable `name` gets the value `Sam`. The inner function can access the value of this variable. When the inner function gets called, `Sam` gets printed. This is how scope works in nested functions.

The bottom line is (and it’s worth repeating) – Enclosed functions can access the variables of enclosing functions.

Keeping this in mind, let’s move on to Python closures.

### Python Closures

In the example above, we have called the inner function inside the outer function. The inner function becomes a closure when we return the inner function instead of calling it.

So we have a closure in Python if-

- We have a nested function, i.e. function within a function
- The nested function refers to a variable of the outer function
- The enclosing function returns the enclosed function

For Example

```python
def outer_func(name):
    # this is the enclosing function

    def inner_func():
        # this is the enclosed function
        # the inner function accessing the outer function's variable 'name'
        print(name)

    return inner_func

# call the enclosing function
myFunction = outer('Sam')
myFunction()
```

**Output**

        Sam

Here, the call to outer function returns the inner function. This then gets assigned to ‘myFunction’. Now when we call myFunction, it prints ‘TechVidvan’ (which was earlier given as an argument to outer).

Even after ‘outer’ finishes its execution and all its variables go out of scope, the value passed to its argument is still remembered.

This is the beauty of closures! We can access the values of a function that no longer exists.

### When and Why do you need to use Closures in Python?

You can use closures

- To replace the unnecessary use of class: Suppose you have a class that contains just one method besides the `__init__` method. In such cases, it is often more elegant to use a closure instead of a class.
- To avoid the use of the global scope: If you have global variables which only one function in your program will use, think closure. Define the variables in the outer function and use them in the inner function.
- To implement data hiding: The only way to access the enclosed function is by calling the enclosing function. There is no way to access the inner function directly.
- To remember a function environment even after it completes its execution: You can then access the variables of this environment later in your program.

[^1]: This module is a work in progress and new files will be added as this and directories will be added to this module.
