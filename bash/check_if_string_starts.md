# How to check if a string starts with a specific value

```bash
var="How to do it?"
if [[ $var == How* ]]; then echo "It starts with How"; fi
```

- var="How to do it?" - define test string to check
- $var == How* - check if ```$var``` starts with ```"How"```
-  echo "It starts with How" - execute this code if ```$var``` really starts with ```How```

group: compare_strings
