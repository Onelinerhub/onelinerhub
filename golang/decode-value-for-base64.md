# Decode value for base64

```go
package main
import (
  b64 "encoding/base64"
  "fmt"
)

func main() {
  bytes,_ := b64.StdEncoding.DecodeString("SGk=")
  str := string(bytes)
}
```

- `b64 "encoding/base64"` - load module to work with base64
- `b64.StdEncoding.DecodeString` - decodes given base64 string to bytes
- `"SGk="` - sample base64 string to decode
- `string(bytes)` - convert resulting bytes to string

group: base64

## Example: 
```go
package main
import (
  b64 "encoding/base64"
  "fmt"
)

func main() {
  bytes,_ := b64.StdEncoding.DecodeString("SGk=")
  str := string(bytes)
  fmt.Println(str)
}
```
```
Hi

```

