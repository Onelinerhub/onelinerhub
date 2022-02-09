# Convert byte to string

```go
str := string(byte)
```

- `str` - string variable
- `string` - converts specified byte to string
- `byte` - byte to convert to string

group: convert

## Example: 
```go
package main
import "fmt"

func main() {
  var bt byte = 97
  str := string(bt)
  fmt.Println(str)
}
```
```
a

```

