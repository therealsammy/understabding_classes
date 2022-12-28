# Understanding Python First Class Functions, Closures, Classes, And Unit Tests.

This module shows fundermental and intermediate concepts of the `Python` programming language. [^1]

The topics are:

- First class functions
- Closures
- Classes & Inheritance
- Unit Tests
- Doctess

This is written for educational purposes.

## [First Class Functions](www.geeksforgeeks.org)

First class objects in a language are handled uniformly throughout. They may be stored in data structures, passed as arguments, or used in control structures. A programming language is said to support first-class functions if it treats functions as first-class objects. Python supports the concept of First Class functions.

A first-class function is not a particular kind of function. All functions in Python are first-class functions.

### Properties of first class functions:

- A function is an instance of the Object type.
- You can store the function in a variable.
- You can pass the function as a parameter to another function.
- You can return the function from a function.
- You can store them in data structures such as hash tables, lists.

> To say that functions are first-class in a certain programming language means that they can be passed around and manipulated similarly to how you would pass around and manipulate other kinds of objects (like integers or strings). You can assign a function to a variable, pass it as an argument to another function, etc. The distinction is not that individual functions can be first class or not, but that entire languages may treat functions as first-class objects, or may not. [BrenBran - StackOverflow](https://stackoverflow.com/a/27392443)

### Examples illustrating First Class functions in Python

1. **Functions are objects**: Python functions are first class objects. In the example below, we are assigning function to a variable. This assignment doesn’t call the function. It takes the function object referenced by shout and creates a second name pointing to it, yell.

```python
# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()
  
print (shout('Hello'))
  
yell = shout
  
print (yell('Hello'))
```

**Output:**

    HELLO
    HELLO

2. **Functions can be passed as arguments to other functions:** Because functions are objects we can pass them as arguments to other functions. Functions that can accept other functions as arguments are also called higher-order functions. In the example below, we have created a function greet which takes a function as an argument.

```python
# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()
  
def whisper(text):
    return text.lower()
  
def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function
                    passed as an argument.""")
    print (greeting) 
  
greet(shout)
greet(whisper)
```

**Output:**

    HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
    hi, i am created by a function passed as an argument.

3. **Functions can return another function:** Given that functions are objects we can return a function from another function. In the below example, the create_adder function returns adder function.

```python
# Python program to illustrate functions
# Functions can return another function
  
def create_adder(x):
    def adder(y):
        return x+y
  
    return adder
  
add_15 = create_adder(15)
  
print (add_15(10))
```

**Output:**

    25

In essence, FCF's are variables of the type 'function' (or variables which point to a function). You can do with them everything you can do with a 'normal' variable.

This is an extremely useful tool as they open the door to other topics dissused in this modules, like `closures`.

## [Closures](techvidan.com)

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

###### [^1]: This module is a work in progress and new files will be added as this and directories will be added to this module.
