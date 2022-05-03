# Create a repeat-until loop

```lua
a = 10
repeat
   print("value of a:", a)
   a = a + 1
until( a > 15 )
```

- `a = 10` - initialize a local variable a with value = 10
- `repeat` - execute the statements following the repeat
- `print("value of a:", a)` - as an example, print statement is shown
- `until( a > 15 )` - the statements after repeat keeps on executing till the statement within the paranthesis with until evaluates to false
- `a = a + 1` - it is necessary to change the value of the variable which is used to check for looping condition. This must evaluates to false at some point, failing which the loop will keep on running forever

group: loop


link_youtube: https://youtu.be/0fA3jBV4uFE
