# How to generate MD5 hash from string

```go
package main

import (
  "fmt"
  "crypto/md5"
)

func main() {
  str := "Hi all!"

  hash := md5.Sum( []byte(str) )
  
  fmt.Printf("%x", hash)
}
```

- `package main` - default package declaration
- `"crypto/md5"` - package to calculate MD5 hashes
- `"Hi all!"` - sample string to hash
- `md5.Sum` - return MD5 hash from given value

group: hash

## Example: 
```go
package main

import (
  "fmt"
  "crypto/md5"
)

func main() {
  str := "Hi all!"

  hash := md5.Sum( []byte(str) )
  
  fmt.Printf("%x", hash)
}
```
```
5dacac312d01035077bc8fdd62f1c361
```

