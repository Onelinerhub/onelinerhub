# Using OR operator

```go
package main

import (
  "fmt"
)

func main() {
  X := true
  Y := false
  
  xor := X || Y
}
```

- `||` - logical `OR` operator

group: logical

## Example: 
```go
package main

import (
  "fmt"
)

func main() {
  X := true
  Y := false
  
  fmt.Println(X || Y)
}
```
```
true

```

