# How to get argument from user

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--manual", help="return the manual", nargs="*", default="default_value")
args = parser.parse_args()
# you can access the argument value with args.manual
```

- argparse - library that handle user arguments
- parser - instance of ArgumentParser
- add_argument - add argument with this function
- -m - short form of argument flag
- --manual - long form of argument flag
- help - help message for this argument
- nargs - can be a number which means user should pass that amount of input or '*' which means any amount of input
- default - default value of this argument
