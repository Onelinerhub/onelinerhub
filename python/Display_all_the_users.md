# Display list of all the users on Unix-like systems

```python -c "print '\n'.join(line.split(':',1)[0] for line in open('/etc/passwd'))"
```

- Have to be root
