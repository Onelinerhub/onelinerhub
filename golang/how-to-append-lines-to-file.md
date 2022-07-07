# How to append line to file

```go
package main

import (
	"os"
)

func main() {
	f, _ := os.OpenFile("/tmp/go.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
  defer f.Close()
  f.WriteString("new line\n")
}
```

- `package main` - default package declaration
- `"os"` - include operating-system level library
- `func main() {` - declare `main` function that will be launched automatically
- `os.OpenFile` - opens file handler
- `/tmp/go.txt` - path to file to open
- `os.O_APPEND|os.O_CREATE|os.O_WRONLY` - permissions used to append to file
- `0644` - file permissions to set
- `defer f.Close()` - deferred file handler close
- `WriteString` - writes string to a given file

group: file

## Example: 
```go
package main

import (
	"os"
)

func main() {
	f, _ := os.OpenFile("/tmp/go.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
  defer f.Close()
  f.WriteString("new line\n")
}
```

