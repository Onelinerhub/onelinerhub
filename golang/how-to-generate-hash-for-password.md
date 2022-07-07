# How to generate hash for password

```go
package main

import (
  "fmt"
  "golang.org/x/crypto/bcrypt"
)

func main() {
  pwd := "qwerty123"
  hash, _ := bcrypt.GenerateFromPassword([]byte(password))
  print(string(hash))
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
  "golang.org/x/crypto/bcrypt"
)

func main() {
  pwd := "qwerty123"
  hash, _ := bcrypt.GenerateFromPassword([]byte(password))
  print(string(hash))
}
```

