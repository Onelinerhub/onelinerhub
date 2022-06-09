# How to format float

```go
package main
import "fmt"

func main() {
  res := fmt.Sprintf("Float: %.2f", 123.32)
  fmt.Println(res)
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `fmt.Sprintf(` - formats given string based on a given template and return result
- `%.2f` - sample float formatting template (leaves 2 decimals)
- `123.32` - sample float number to format

group: float_format

## Example: 
```go
package main
import "fmt"

func main() {
  res := fmt.Sprintf("Float: %.2f", 123.32)
  fmt.Println(res)
}
```
```
Float: 123.32

```

