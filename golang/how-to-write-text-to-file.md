# How to write text to file

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
    fmt.Println(string(t))
  }
}
```
```
hello go!

```

