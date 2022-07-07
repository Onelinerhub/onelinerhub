# How to generate hash for password

### Use **`bcrypt`** package (to install run `go get golang.org/x/crypto/bcrypt`) for hashin passwords:

```go
package main

import (
  "fmt"
  "golang.org/x/crypto/bcrypt"
)

func main() {
  pwd := "qwerty123"
  hash, _ := bcrypt.GenerateFromPassword([]byte(pwd), 10)
  fmt.Println(string(hash))
}
```

- `package main` - default package declaration
- `"golang.org/x/crypto/bcrypt"` - 
- `qwerty123` - sample password string to hash
- `bcrypt.GenerateFromPassword` - returns hash from given password

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
  hash, _ := bcrypt.GenerateFromPassword([]byte(pwd), 10)
  fmt.Println(string(hash))
}
```
```
$2a$10$bTduN3NrqqLlJaPdG1HULe4mdZc3Fh1RvDQ1qC4NCi3xuAMiVs.sC

```

