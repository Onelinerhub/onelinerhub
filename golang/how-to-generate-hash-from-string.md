# How to generate hash from string

```go
package main

import (
  "fmt"
  "hash/fnv"
)

func main() {
  str := "Hi all!"

  h := fnv.New32a()
  h.Write([]byte(str))
  hash := h.Sum32()
}
```

- `package main` - default package declaration
- `"hash/fnv"` - package to work with hashes
- `"Hi all!"` - sample string to hash
- `fnv.New32a()` - creates new 32-bit FNV-1a hashing object
- `.Write([]byte(str))` - write our string to hashing object
- `.Sum32()` - calculate hash value

group: hash

## Example: 
```go
package main

import (
  "fmt"
  "hash/fnv"
)

func main() {
  str := "Hi all!"

  h := fnv.New32a()
  h.Write([]byte(str))
  hash := h.Sum32()
  
  fmt.Println(hash)
}
```
```
3458820852

```

