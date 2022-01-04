# Remove Duplicate Sentences(line) From String
```python
lines_seen = set()
with open("output.txt", "w") as output_file:
	for each_line in open("input.txt", "r"):
	    if each_line not in lines_seen:
	        output_file.write(each_line)
	        lines_seen.add(each_line)
```

Read .txt File and Remove Duplicate Sentences(line) From String