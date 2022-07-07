# How to generate UUID as string

### This uses [uuid](https://pkg.go.dev/github.com/google/uuid#section-readme) module that should be installed by `go get github.com/google/uuid` command:

```go
package main

import "fmt"
import "github.com/google/uuid"

func main() {
  string_uuid = (uuid.New()).String()
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
  string_uuid := (uuid.New()).String()
  fmt.Println( string_uuid )
}
```
```
2ba2d6aa-e84e-424d-82cb-96f1c951f5d2

```

