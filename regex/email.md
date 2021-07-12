# Validate email address

```regex
/^[^\s@]+@[^\s@]+\.[^\s@]+$/
```

- /^ - begin from the start of the string
- \[^\s@\]+ - match everything escept whitespaces and `@` symbol ([suggested here](https://stackoverflow.com/a/9204568/15840728))
