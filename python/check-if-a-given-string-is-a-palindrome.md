# Check if a given string is a palindrome

```python
def is_palindrome(word):
    return word.lower() == word[::-1].lower()

print(palindrome("Racecar"))
```

- `is_palindrome(` - function name to check if the string is a palindrome
- `.lower(` - converts the string to lowercase
- `word[::-1]` - reverses the string
- `return` - returns `True` if the string is a palindrome

## Example: 
```python
print(is_palindrome("Racecar"))
```
```
True

```
