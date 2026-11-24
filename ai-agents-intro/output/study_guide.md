# Topic: Python decorators

## Simple Explanation

A decorator is a function that takes another function and adds extra behaviour to it without changing its code. You apply it by writing @decorator_name on the line above a function definition.

## Key Concepts

- Functions are objects: they can be passed to other functions and returned from them.
- A decorator takes a function and returns a new function.
- The @ syntax is a shortcut for func = decorator(func).
- A wrapper function runs code before and after the original function.
- functools.wraps keeps the original function's name and docstring.

## Example

    def shout(func):
        def wrapper():
            print("Before the call")
            func()
            print("After the call")
        return wrapper


    @shout
    def hello():
        print("Hello!")


    hello()

## Practice Exercise

**Exercise:** Write a decorator called log_call that prints "Calling <function name>" before running the function it decorates.

**Expected input:** A function named greet that prints "Hi".

**Expected output:** The lines "Calling greet" then "Hi".

**Hints:** Use func.__name__ to get the function's name. Remember to call the original function inside the wrapper.

## Common Mistakes

- Forgetting to return the wrapper function from the decorator.
- Forgetting to call the original function inside the wrapper.
- Writing @decorator() instead of @decorator when the decorator takes no arguments.

## Review Comments

**Missing information:** The guide does not show how to pass arguments through the wrapper.

**Unclear parts:** The shortcut func = decorator(func) could use a short example.

**Suggestions:** Add *args and **kwargs to the wrapper in the example, and mention functools.wraps in the code.

**Recommendation:** Approve. The structure is clear and the exercise is small enough for a beginner.

## Final Summary

This guide explained Python decorators with key concepts, an example, a practice exercise and common mistakes, and it was checked by a reviewer.
