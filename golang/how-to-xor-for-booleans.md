# How to XOR for booleans

```go
package main

import (
  "fmt"
)

func main() {
  X := true
  Y := false
  
  xor := (X || Y) && !(X && Y)
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `(X || Y) && !(X && Y)` - logical `XOR` representation instead of mission operator

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
  
  fmt.Println((X || Y) && !(X && Y))
}
```
```
true

```

