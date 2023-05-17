# How to replace in a file using Python regex?
// plain

Regex (Regular Expressions) can be used to replace text in a file using Python.

```
import re

# open the file
f = open('file.txt', 'r')

# read the file
text = f.read()

# close the file
f.close()

# replace the text
text = re.sub('old_text', 'new_text', text)

# open the file
f = open('file.txt', 'w')

# write the new text
f.write(text)

# close the file
f.close()
```

The example code above will open a file, read the contents, replace the text, and write the new text back to the file.

## Code explanation


1. `import re` - imports the regular expression module
2. `f = open('file.txt', 'r')` - opens the file in read mode
3. `text = f.read()` - reads the contents of the file
4. `f.close()` - closes the file
5. `text = re.sub('old_text', 'new_text', text)` - replaces the text using the regular expression module
6. `f = open('file.txt', 'w')` - opens the file in write mode
7. `f.write(text)` - writes the new text to the file
8. `f.close()` - closes the file

## Helpful links

- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html)

onelinerhub: [How to replace in a file using Python regex?](https://onelinerhub.com/python-regex/how-to-replace-in-a-file-using-python-regex)