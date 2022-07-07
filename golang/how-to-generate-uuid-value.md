# How to generate UUID value 

### This uses [uuid](https://pkg.go.dev/github.com/google/uuid#section-readme) module that should be installed by `go get github.com/google/uuid` command:

```go
package main

import "fmt"
import "github.com/google/uuid"

func main() {
  uid = uuid.New()
  string_uuid = uid.String()
}
```

- `github.com/google/uuid` - module to work with [uuid](https://pkg.go.dev/github.com/google/uuid#section-readme)
- `uuid.New()` - init new UUID value
- `.String()` - converts generated UUID to string

group: uuid

## Example: 
```go
package main

import "fmt"
import "github.com/google/uuid"

func main() {
  fmt.Println( (uuid.New()).String() )
}
```
```
1755c133-b8c6-4783-9fc6-9fcb0b6dcc27

```

