# How to format float

```go
package main
import "fmt"

func main() {
  res := fmt.Sprintf("%f is %d", 123.32)
  fmt.Println(res)
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `fmt.Sprintf(` - formats given string based on a given template and return result
- `res` - variable will contain formatted string

group: float_format

## Example: 
```go
package main
import "fmt"

func main() {
  res := fmt.Sprintf("%f is %d", 123.32)
  fmt.Println(res)
}
```
```
A is 12

```

