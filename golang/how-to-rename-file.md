# How to remove file

```go
package main

import (
	"os"
)

func main() {
  os.Remove("/path/to/file")
}
```

- `package main` - default package declaration
- `"os"` - include operating-system level library
- `func main() {` - declare `main` function that will be launched automatically
- `os.Remove(` - removes specified file
- `/path/to/file` - path to file to remove

group: file

## Example: 
```go
package main

import (
  "fmt"
	"os"
)

func main() {
  e := os.Remove("/tmp/go2.txt")
  fmt.Println(e)
}
```
```
<nil>
```

