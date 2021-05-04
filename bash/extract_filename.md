# How to extract file name

```bash
filepath=/tmp/test.php
file=$(basename -- "$filepath")
name="${file%.*}"
```

- file=$(basename -- "$filepath") - will extract ```test.php```
- name="${file%.*}" - will extract ```test```
