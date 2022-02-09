# Encode value to base64

```go
package main
import (
  b64 "encoding/base64"
  "fmt"
)

func main() {
  str := b64.StdEncoding.EncodeToString([]byte("Hi"))
}
```

- `b64 "encoding/base64"` - load module to work with base64
- `b64.StdEncoding.EncodeToString` - encodes given bytes into base64 string
- `[]byte` - convert given string to bytes 
- `"Hi"` - sample string to encode into base64

group: base64

## Example: 
```go
package main
import (
  b64 "encoding/base64"
  "fmt"
)

func main() {
  str := b64.StdEncoding.EncodeToString([]byte("Hi"))
  fmt.Println(str)
}
```
```
SGk=

```

