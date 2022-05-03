# How to write to file

```lua
file = io.open('/tmp/hi.txt', 'w')
file:write('hello!')
io.close(file)
```

- `io.open` - opens file handler
- `/tmp/hi.txt` - path to file to write
- `'w'` - open file in writing mode
- `file:write` - write specified text to file
- `'hello!'` - sample text to write to file
- `io.close` - closes file handler

group: files

## Example: 
```lua
file = io.open('/tmp/hi.txt', 'w')
file:write('hello!')
io.close(file)

for line in io.lines ('/tmp/hi.txt') do print(line) end
```
```
hello!

```

link_youtube: https://youtu.be/ljETu8uYVH4
