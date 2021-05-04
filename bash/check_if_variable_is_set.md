# How to check if variable is set or unset

```bash
if [ -z ${variable+x} ]; then echo "\$variable is not set"; else echo "\$variable is set"; fi
```

- variable - name of varible we're checking
- echo "\$variable is not set" - will execute if variable is not set
- echo "\$variable is set" - will execute if variable is set, even if it's empty (```variable=""```)

group: empty_or_unset_variables
