# Check if a string contains a substring

```bash
string="Haystack with a needle"
if [[ $string == *"needle"* ]]; then echo "Found"; fi
```

- string="Haystack with a needle" - test string to search in
- "needle" - substring we're searching for in a test string
- echo "Found" - replace with any code that should be executed if the string contains required substring
