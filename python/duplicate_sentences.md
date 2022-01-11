# Remove duplicate lines from text file

### We'll remove duplicate lines from `input.txt` and write result to `output.txt`

```python
lines_seen = set()
with open('output.txt', 'w') as output_file:
	for each_line in open('input.txt', 'r'):
	    if each_line not in lines_seen:
	        output_file.write(each_line)
	        lines_seen.add(each_line)
```

- `lines_seen` - declare set to store unique lines
- `with open` - opens specified file for reads
- `if each_line not in lines_seen` - check if this line is duplicate
- `output_file.write` - write unique line to `output.txt`
- `lines_seen.add` - save unique line to seen lines


