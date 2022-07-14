# How to get single character substring from string

```go
package main
import "fmt"
func main() {
  str := "some val!"
  fmt.Println(string(str[6]))
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `"some val!"` - sample string
- `str[6]` - gets single character from position `6` of the string
- `string(` - convert given variable to string

group: substring

## Example: 
```go
package main
import "fmt"
func main() {
  str := "some val!"
  fmt.Println(string(str[6]))
}
```
```
a

```

