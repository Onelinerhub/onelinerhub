# How to check if variable is empty

```bash
if [ -z "$variable" ]; then echo "\$variable is empty"; else echo "\$variable is not empty"; fi
```

- variable - name of varible we're checking
- echo "\$variable is empty" - will execute if variable is empty or unset
- echo "\$variable is not empty" - will execute if variable is not empty (has some value)

group: empty_or_unset_variables
