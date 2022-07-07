# How to generate sha256 hash from string

```go
package main

import (
  "fmt"
  "crypto/sha256"
)

func main() {
  str := "Hi all!"

  h := sha256.New()
  h.Write([]byte(str))
  hash := h.Sum(nil)
  
  fmt.Printf("%x", hash)
}
```

- `package main` - default package declaration
- `"hash/fnv"` - package to work with hashes
- `"Hi all!"` - sample string to hash
- `sha256.New()` - new shad56 hasher
- `h.Write([]byte(str))` - pass our string to hasher
- `h.Sum(nil)` - calculate and return hash

group: hash

## Example: 
```go
package main

import (
  "fmt"
  "crypto/sha256"
)

func main() {
  str := "Hi all!"

  h := sha256.New()
  h.Write([]byte(str))
  hash := h.Sum(nil)
  
  fmt.Printf("%x", hash)
}
```
```
c21956890779e4c284362ac82f5e846f67571d5736fe6b040bebb38283d23766
```

