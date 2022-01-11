# Remove Duplicate Words From String
```python
fname = "input.txt"
fhand = open(fname)
AllWords = list()
ResultList = list()

for line in fhand:
    line.rstrip()
    words = line.split()
    AllWords.extend(words)

AllWords.sort()

for word in AllWords:
    if word not in ResultList:
        ResultList.append(word)

with open('output.txt', 'w') as filehandle:
    for listitem in ResultList:
        filehandle.write('%s\n' % listitem)

print(ResultList)
```

Read .txt File and Remove Duplicate Words From String