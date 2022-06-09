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
- `%10d` - sample number formatting placeholder, will pad number to 10 spaces on the left 
- `123` - sample integer value to format

group: int_format

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

