# How to overwrite content in file if it exists

```go
package main

import (
	"os"
)

func main() {
	f, _ := os.OpenFile("/tmp/go.txt", os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0644)
  defer f.Close()
  f.WriteString("new content\n")
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
  "fmt"
	"os"
)

func main() {
	f, _ := os.OpenFile("/tmp/go.txt", os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0644)
  defer f.Close()
  f.WriteString("new content\n")
  
  t, _ := os.ReadFile("/tmp/go.txt")
  fmt.Println(string(t))
}
```
```
new content


```

