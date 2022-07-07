# How to read file to bytes array

```go
package main

import (
	"os"
)

func main() {
  bytes, _ := os.ReadFile("/var/www/examples/test.txt")
}
```

- `package main` - default package declaration
- `"os"` - include operating-system level library
- `func main() {` - declare `main` function that will be launched automatically
- `os.ReadFile(` - read contents from specified file
- `/var/www/examples/test.txt` - file to read
- `bytes` - will contain list of bytes that were read from file

group: file

## Example: 
```go
package main

import (
  "fmt"
	"os"
	"reflect"
)

func main() {
  bytes, _ := os.ReadFile("/var/www/examples/test.txt")
  fmt.Println(bytes)
  fmt.Println(reflect.TypeOf(bytes))
}
```
```
[104 105 33 10]
[]uint8

```

