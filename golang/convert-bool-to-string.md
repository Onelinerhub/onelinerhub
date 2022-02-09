# Convert bool to string

```go
package main
import "strconv"

func main() {
  str := strconv.FormatBool(false))
}
```

- `str :=` - will contain string representation of given boolean value
- `FormatBool` - converts given boolean to string
- `false` - sample boolean to convert

group: convert

## Example: 
```go
package main
import (
  "fmt"
  "strconv"
)

func main() {
  var str string
  str = strconv.FormatBool(false)
  fmt.Println(str)
}
```
```
false

```

