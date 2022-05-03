# How to open file

```lua
file = io.open('/var/www/examples/test.txt', 'r')
io.close(file)
```

- `io.open` - opens file handler
- `/var/www/examples/test.txt` - path to the file to open
- `'r'` - mode to open file in (`r` to read, `w` to write)
- `file` - file handler
- `io.close` - closes file handler

group: files

## Example: 
```lua
file = io.open ('/var/www/examples/test.txt', 'r')
print(file:read())
io.close(file)
```
```
hi!

```

link_youtube: https://youtu.be/uwF7cZRerxM
