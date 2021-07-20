# Match html tags

```regex
/<([a-z]+)[^>]*>/
```

- /< - open tag at the beginning
- \[a-z\]+ - any number of any letter
- \[^>\]* - will also include attributes if any (any text before closing tag `>`)
- consider using [HTML parsers](https://www.google.com/search?q=html+parser) for better support
