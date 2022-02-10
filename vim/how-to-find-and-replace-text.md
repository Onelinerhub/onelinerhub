# How to find and replace text

### Press `Esc` to [switch to command mode](/vim/how-to-switch-to-command-mode) and then type (then press `Enter`):

```text
:<range>s/<target>/<dest>/<flags>
n
N
```

- ``:`` - tells Vim we are gonna input a command
- ``<range>`` - the range to match text (by default the line where the cursor is. ``%`` for the whole file)
- ```s``` - character used to indicate "find and replace"
- ``<target>`` - the string(s) we want to replace (regular expressions can be used)
- ``<dest>`` - the string we want the match(es) to be converted to
- ``<flags>`` - the flags for the search ("g" = "replace all", "i" = "case insensitive", and "c" = "ask confirmation")
- ```n``` - replace the next match in the range
- ```N``` - replace the first match in the range before the cursor
- ```/``` - used to separate the parameters, can be any unicode character

## Example: 
```text
-----------
Goods are
good things
-----------

[Esc] :%s/good/awesome/gi

```
```
awesomes are
awesome things
```

