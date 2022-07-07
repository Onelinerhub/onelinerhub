# How to validate hashed password

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
  
  if ( bcrypt.CompareHashAndPassword(hash, []byte("qwerty123")) == nil ) {
    fmt.Println("password is correct")
  }
}
```

- `package main` - default package declaration
- `"golang.org/x/crypto/bcrypt"` - 
- `qwerty123` - sample password string to hash
- `bcrypt.GenerateFromPassword` - returns hash from given password
- `CompareHashAndPassword` - compares given hash (generated early) and password value (e.g., posted from client), returns error if they don't match

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
  
  if ( bcrypt.CompareHashAndPassword(hash, []byte("qwerty123")) == nil ) {
    fmt.Println("password is correct")
  }
}
```
```
password is correct

```

