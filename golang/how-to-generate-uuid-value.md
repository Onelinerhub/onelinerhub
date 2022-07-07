# How to generate UUID value 

### This uses [uuid](https://pkg.go.dev/github.com/google/uuid#section-readme) module that should be installed by `go get github.com/google/uuid` command:

```go

```


group: uuid

## Example: 
```go
package main

import "fmt"
import "github.com/google/uuid"

func main() {
  fmt.Println( uuid.New() )
}
```

