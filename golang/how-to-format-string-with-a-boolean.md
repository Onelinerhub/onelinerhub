# How to format string with a boolean

```go
package main
import "fmt"

func main() {
  res := fmt.Sprintf("%t is bool", true)
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `fmt.Sprintf(` - formats given string based on a given template and return result
- `res` - variable will contain formatted string

group: string_format

## Example: 
```go
package main
import "fmt"

func main() {
  res := fmt.Sprintf("%t is bool", true)
}
```
```
A is 12

```

