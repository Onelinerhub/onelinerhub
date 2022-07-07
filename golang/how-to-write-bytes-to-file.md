# How to write bytes to file

```go
package main

import (
	"os"
)

func main() {
	s := []byte("hello go!")
  os.WriteFile("/tmp/go.txt", s, 0755)
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `"os"` - include operating-system level library
- `[]byte("hello go!")` - sample bytes to write to file
- `os.WriteFile` - write specified content to given file
- `/tmp/go.txt` - path to file to write content to
- `0755` - set file permissions after writing

group: file

## Example: 
```go
package main

import (
  "fmt"
	"os"
)

func main() {
	s := []byte("hello go!")
  os.WriteFile("/tmp/go.txt", s, 0755)
  
  t, e := os.ReadFile("/tmp/go.txt")
  if e == nil {
    fmt.Println(t)
  }
}
```
```
[104 101 108 108 111 32 103 111 33]

```

