# Find all URLs in a string

replace `string` with you string or variable
```python
import re
all_links = re.findall(r"((http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?)", string)
```

- re - python regex library
- all_links - contain list of tuple(s). tuple(s) contain: 0th index -> URL, 1st index -> protocol, 2nd index -> main domain, 3rd index -> path.
- string - input string to search for URLs

## Example
```python
string = 'https://onelinerhub.com/python/if_else hello this is onelinerhub,https://github.com/'
```
```python
[('https://onelinerhub.com/python/if_else', 'https', 'onelinerhub.com', '/python/if_else'), ('https://github.com/', 'https', 'github.com', '')]
```
