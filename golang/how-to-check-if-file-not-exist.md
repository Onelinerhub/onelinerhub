# How to check if file not exist

```go
package main

import (
  "fmt"
  "errors"
	"os"
)

func main() {
  if _, err := os.Stat("/no/such/file"); errors.Is(err, os.ErrNotExist) {
    fmt.Println("no such file")
  }
}
```

- `package main` - default package declaration
- `"os"` - include operating-system level library
- `func main() {` - declare `main` function that will be launched automatically
- `os.Stat` - retrieve file stats
- `errors.Is` - check if raised error is of specified type
- `ErrNotExist` - raises when there are no such file

group: file

## Example: 
```go
package main

import (
  "fmt"
  "errors"
	"os"
)

func main() {
  if _, err := os.Stat("/no/such/file"); errors.Is(err, os.ErrNotExist) {
    fmt.Println("no such file")
  }
}
```
```
no such file

```

