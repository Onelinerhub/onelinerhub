# How to split a string with a delimiter

```bash
string="line1;line2;line3"
for line in $(echo $string | tr ";" "\n"); do echo $line; done
```

- string="line1;line2;line3" - test string to split by ```;```
- echo $IN | tr ";" "\n" - changes ```;``` to ```\n``` symbol in ```$string```
- echo $line - prints echo line in cycle, previously splitted by ```;```, replace with your code
