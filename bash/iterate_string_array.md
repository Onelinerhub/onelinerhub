# How to iterate through an array of strings

```bash
declare -a arrary=("string1" "string2" "string3")
for i in "${array[@]}"; do echo "$i"; done
```

- `declare -a arrary` - create test array of strings
- `for i in "${array[@]}";` - iterate through ```$array```
- `echo "$i"` - replace with your code to manipulate on each array element


link_youtube: https://youtu.be/K4zkN5f5oQQ
