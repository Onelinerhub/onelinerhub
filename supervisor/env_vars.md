# Set environment variables for specific process

```ini
[program:prcs]
...
environment=VAR="1",VAR2="2"
```

- \[program:prcs\] - process config section
- environment= - specifies environment variables to set for this process
- VAR="1" - first env variable and it's value
- VAR2="2" - second end variable and it's value
