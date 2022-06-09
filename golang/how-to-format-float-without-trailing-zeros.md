# How to format float without trailing zeros

```go
package main
import "fmt"

func main() {
  res := fmt.Sprintf("Float: %.1f", 123.3)
  fmt.Println(res)
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `fmt.Sprintf(` - formats given string based on a given template and return result
- `%.1f` - sample float formatting template (leaves 1 decimals, removes trailing zeroa)
- `123.3` - sample float number to format
- `fmt.Println` - prints specified string

group: float_format

## Example: 
```go
package main
import "fmt"

func main() {
  res := fmt.Sprintf("Float: %.1f", 123.3)
  fmt.Println(res)
}
```
```
Float: 123.3

```

