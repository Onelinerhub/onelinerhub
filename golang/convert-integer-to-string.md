# Convert integer to string

```go
package main
import "strconv"

func main() {
  str := strconv.FormatInt(123, 10)
}
```

- `str :=` - will contain string representation of a given number
- `FormatInt` - converts specified integer to string
- `123` - number to convert to string
- `10` - base to convert base on (standard `base-10` number)

group: convert

## Example: 
```go
package main
import (
  "fmt"
  "strconv"
)

func main() {
  str := strconv.FormatInt(123, 10)
  fmt.Println(str)
}
```
```
123

```

