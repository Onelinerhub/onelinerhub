# Using AND operator

```go
package main

import (
  "fmt"
)

func main() {
  X := true
  Y := false
  
  xor := X && Y
}
```

- `&&` - logical `AND` operator

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
  
  fmt.Println(X && Y)
}
```
```
false

```

