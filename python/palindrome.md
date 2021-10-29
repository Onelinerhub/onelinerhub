# Palindrome
```python
def palindrome(word):
    return word.lower() == word[::-1].lower()

print(palindrome("Racecar"))
```

- palindrome() - function which takes the string as argument
- .lower() - converts the string to lowercase
- word[::-1] - reverses the string
- return - returns true if the string is a Palindrome
