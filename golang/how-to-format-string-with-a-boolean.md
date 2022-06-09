# How to format string with a boolean

```go
package main
import "fmt"

func main() {
  res := fmt.Sprintf("%t is bool", true)
  fmt.PrintLn(res)
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `fmt.Sprintf(` - formats given string based on a given template and return result
- `%t` - placeholder will return `true` or `false` based on a given boolean value

group: string_format

## Example: 
```go
package main
import "fmt"

func main() {
  res := fmt.Sprintf("%t is bool", true)
  fmt.Println(res)
}
```
```
true is bool

```

