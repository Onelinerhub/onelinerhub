# How to write file line by line

```go
package main

import (
  "bufio"
	"os"
)

func main() {
  lines := []string{"first line", "second line" , "third line"}
	f, _ :=os.OpenFile("/tmp/go.txt", os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0644)
  defer f.Close()
  dw := bufio.NewWriter(f)
  
  for _, l := range lines {
    dw.WriteString(l + "\n")
  }
  
  dw.Flush()
}
```

- `package main` - default package declaration
- `"os"` - include operating-system level library
- `func main() {` - declare `main` function that will be launched automatically
- `lines` - sample slices with 3 text lines to write to file
- `"bufio"` - package to efficiently work with buffers (including writing to files)
- `os.OpenFile` - opens file handler
- `/tmp/go.txt` - path to file to write content to
- `bufio.NewWriter` - create new buffer from specified file handler
- `.WriteString(` - writes specified string to buffer
- `dw.Flush()` - flush buffer (to write changes to file)

group: file

## Example: 
```go
package main

import (
  "bufio"
  "fmt"
	"os"
)

func main() {
	lines := []string{"first line", "second line" , "third line"}
	f, _ := os.OpenFile("/tmp/go.txt", os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0644)
  defer f.Close()
  dw := bufio.NewWriter(f)
  
  for _, l := range lines {
    dw.WriteString(l + "\n")
  }
  
  dw.Flush()
  
  t, _ := os.ReadFile("/tmp/go.txt")
  fmt.Println(string(t))
}
```
```
first line
second line
third line


```

