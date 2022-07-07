# How to check if file exist

```go
package main

import (
  "fmt"
	"os"
)

func main() {
  if _, err := os.Stat("/etc/passwd"); err == nil {
    fmt.Println("file is there!")
  }
}
```

- `package main` - default package declaration
- `"os"` - include operating-system level library
- `func main() {` - declare `main` function that will be launched automatically
- `os.Stat` - retrieve file stats
- `err == nil` - if no error raised - file exists

group: file

## Example: 
```go
package main

import (
  "fmt"
	"os"
)

func main() {
  if _, err := os.Stat("/etc/passwd"); err == nil {
    fmt.Println("file is there!")
  }
}
```
```
file is there!

```

