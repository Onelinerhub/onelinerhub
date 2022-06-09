# How to pad integer with leading zeros

```go
package main
import "fmt"

func main() {
  res := fmt.Sprintf("Number: %08d", 123)
  fmt.Println(res)
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `fmt.Sprintf(` - formats given string based on a given template and return result
- `%08d` - pads given number to 8 zeros on the left
- `123` - sample integer value to format
- `res` - variable will contain formatted value

group: int_format

## Example: 
```go
package main
import "fmt"

func main() {
  res := fmt.Sprintf("Number: %08d", 123)
  fmt.Println(res)
}
```
```
Number: 00000123

```

