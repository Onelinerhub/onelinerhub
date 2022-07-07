# How to rename a file

```go
package main

import (
	"os"
)

func main() {
  os.Rename("current.txt", "new.txt")
}
```

- `package main` - default package declaration
- `"os"` - include operating-system level library
- `func main() {` - declare `main` function that will be launched automatically
- `os.Rename(` - renames specified file
- `current.txt` - old file name
- `"new.txt"` - new file name

group: file


