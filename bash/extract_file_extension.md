# How to extract file extension

```bash
filename=/tmp/test.php
extension="${filename##*.}"
```

- "${filename##*.}" - extracts file extension. Use ```echo $extension``` to print file extension.
