# How to rename file

```go
package main

import (
	"os"
)

func main() {
  os.Rename(old_name, new_name)
}
```

- `package main` - default package declaration
- `"os"` - include operating-system level library
- `func main() {` - declare `main` function that will be launched automatically
- `os.Rename(` - renames given file to a new name
- `old_name` - current file name
- `new_name` - new file name

group: file

## Example: 
```go
package main

import (
  "fmt"
	"os"
)

func main() {
  e := os.Rename("/tmp/go.txt", "/tmp/go2.txt")
  fmt.Println(e)
}
```
```
<nil>

```

