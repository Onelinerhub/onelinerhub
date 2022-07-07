# How to generate sha256 hash from string

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
  "crypto/sha256"
)

func main() {
  str := "Hi all!"

  h := sha256.New()
  h.Write([]byte(str))
  hash := h.Sum(nil)
  
  fmt.Println(string(hash))
}
```
```
[194 25 86 137 7 121 228 194 132 54 42 200 47 94 132 111 103 87 29 87 54 254 107 4 11 235 179 130 131 210 55 102]

```

