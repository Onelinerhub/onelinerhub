# How to format variables within a string 

```go
package main
import "fmt"

func main() {
  a := "Ukraine"
  b := 1
  res := fmt.Sprintf("%s is %d country!", a, b)
  fmt.Println(res)
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `fmt.Sprintf(` - formats given string based on a given template and return result
- `%s is %d country!` - template string to format variables (first - string placeholder, second - decimal placeholder)
- `a, b` - variables to use for formatting (`a` goes to the first placeholder, `b` goes to then second)
- `fmt.Println` - prints specified string

group: string_format

## Example: 
```go
package main
import "fmt"

func main() {
  a := "Ukraine"
  b := 1
  res := fmt.Sprintf("%s is %d country!", a, b)
  fmt.Println(res)
}
```
```
Ukraine is 1 country!

```

