# How to match a URL using Python regex?
// plain

Python regex can be used to match a URL. The following example code block uses the `re.search()` function to match a URL:
```
import re

url = 'https://www.example.com/path/to/page'

match = re.search(r'https?://(www\.)?\w+\.\w+/\S+', url)

if match:
    print(match.group())
```
The output of the example code is:
```
https://www.example.com/path/to/page
```
## Code explanation


- `import re`: imports the `re` module which provides regular expression matching operations.
- `url = 'https://www.example.com/path/to/page'`: assigns the URL to a variable.
- `re.search(r'https?://(www\.)?\w+\.\w+/\S+', url)`: searches for a match of the regular expression pattern in the URL. The pattern consists of the following parts:
  - `https?://`: matches `http` or `https` at the beginning of the URL.
  - `(www\.)?`: matches `www.` at the beginning of the URL, if present.
  - `\w+\.\w+`: matches the domain name.
  - `/\S+`: matches the path of the URL.
- `if match:`: checks if a match was found.
- `print(match.group())`: prints the matched URL.

## Helpful links

- [Python Regular Expression Quick Guide](https://www.rexegg.com/regex-quickstart.html)
- [Python re Module](https://docs.python.org/3/library/re.html)

onelinerhub: [How to match a URL using Python regex?](https://onelinerhub.com/python-regex/how-to-match-a-url-using-python-regex)