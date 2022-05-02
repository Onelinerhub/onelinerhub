# Get formatted date/time

### Find all [formatting options here](https://www.lua.org/pil/22.1.html):

```lua
os.date("at %H:%M on %d %B, %Y")
```

- `os.date` - returns current date formatted by a given string
- `%H` - hour in 00...24 format
- `%M` - minutes
- ` %d` - day
- `%B` - full month name
- `%Y` - full year

group: date_time

## Example: 
```lua
print( os.date("at %H:%M on %d %B, %Y") )
```
```
at 11:05 on 03 February, 2022

```

link_youtube: https://youtu.be/mwVjZARmIIs
