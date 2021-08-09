# How to replace functions with Lambda functions

This function
```python
def sum(foo):
    return foo+foo
```
gives the same output as doing a lambda function like this:
```python
lambda foo: foo+foo
```
This is very useful if you want to create one-use, one-liner functions on a program.

