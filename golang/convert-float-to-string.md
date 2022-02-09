# Convert float to string

```go
package main
import "strconv"

func main() {
  var str string
  str = strconv.FormatFloat(12.3, 'f', 1, 32))
}
```

- `FormatFloat` - converts float to string
- `12.3` - float value to convert to string
- `'f'` - format of a float value (`d.d` in our case)
- `1, 32` - number of digits after the point and input float size (`32` bits in our case)

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
  str = strconv.FormatFloat(12.3, 'f', 1, 32)
  fmt.Println(str)
}
```
```
12.3

```

