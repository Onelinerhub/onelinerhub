# How to read file to string

```go
package main

import (
	"os"
)

func main() {
  t, _ := os.ReadFile("/var/www/examples/test.txt")
  str := string(t)
}
```

- `package main` - default package declaration
- `"os"` - include operating-system level library
- `func main() {` - declare `main` function that will be launched automatically
- `os.ReadFile(` - read contents from specified file
- `/var/www/examples/test.txt` - file to read
- `str` - string variable will contain contents from file
- `string(` - convert given variable to string

group: file

## Example: 
```go
package main

import (
  "fmt"
	"os"
)

func main() {
  t, _ := os.ReadFile("/var/www/examples/test.txt")
  str := string(t)
  fmt.Println(str)
}
```
```
hi!


```

