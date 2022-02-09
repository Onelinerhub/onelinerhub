# Convert bool to string

```go
package main
import "strconv"

func main() {
  var str string
  str = strconv.FormatBool(false))
}
```


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

