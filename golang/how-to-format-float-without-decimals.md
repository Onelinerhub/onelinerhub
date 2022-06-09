# How to format float without decimals

```go
package main
import "fmt"

func main() {
  res := fmt.Sprintf("Float: %.0f", 123.3)
  fmt.Println(res)
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `fmt.Sprintf(` - formats given string based on a given template and return result
- `%.0f` - removes decimals from given float number
- `123.3` - sample float number to format
- `fmt.Println` - prints specified string

group: float_format

## Example: 
```go
package main
import "fmt"

func main() {
  res := fmt.Sprintf("Float: %.0f", 123.3)
  fmt.Println(res)
}
```
```
Float: 123

```

