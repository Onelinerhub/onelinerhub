# Display list of all the users on Unix-like systems

```python
python -c "print('\n'.join(line.split(':',1)[0] for line in open('/etc/passwd')))"
```

- -c - terminates the option list (following options are passed as arguments to the command).
- line.split - splits a string by a seperator.
- etc/passwd - displays the user information.
