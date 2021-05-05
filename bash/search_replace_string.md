# How to search and replace string in variable

```bash
haystack="Bash is so so"
search="so so"
replace="good"
echo "${haystack/$search/$replace}"
```

- haystack="Bash is so so" - the string to do the search and replace in
- search="so so" - variable with the search text
- replace="good" - variable with the replace text

group: replace_strings
