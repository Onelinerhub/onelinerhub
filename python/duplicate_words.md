# Remove duplicate words from string

```python
words = 'a b c b c'.split()
uniq = list()

for word in words:
  if word not in uniq:
    uniq.append(word)

uniq_string = ' '.join(uniq)
```

- `'a b c b c'` - sample string to remove duplicate words from
- `.split()` - will split given string into a list of words
- `for word in words` - iterate through all words
- `uniq.append(word)` - append `word` to `uniq` list if it's not in the list already
- `uniq_string` - final string without duplicate words

group: remove_duplicates

## Example: 
```python
words = 'hello hi hello you all'.split()
uniq = list()

for word in words:
  if word not in uniq:
    uniq.append(word)

print(' '.join(uniq))
```
```
hello hi you all

```

