# How to format integer

```go
package main
import "fmt"

func main() {
  res := fmt.Sprintf("Number: %10d", 123)
  fmt.Println(res)
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `fmt.Sprintf(` - formats given string based on a given template and return result
- `%t` - placeholder will return `true` or `false` based on a given boolean value
- `true` - sample boolean value to format

group: string_format

## Example: 
```go
package main
import "fmt"

func main() {
  res := fmt.Sprintf("Number: %10d", 123)
  fmt.Println(res)
}
```
```
Number:        123

```

