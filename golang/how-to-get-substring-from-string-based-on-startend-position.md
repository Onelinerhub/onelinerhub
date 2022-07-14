# How to get substring from string based on start/end position

```go
package main
import "fmt"
func main() {
  str := "some val!"
  fmt.Println(str[5:7])
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `"some val!"` - sample string
- `str[5:7]` - extracts substring from position `5` and ends on position `7` (2-character string as a result)

group: substring

## Example: 
```go
package main
import "fmt"
func main() {
  str := "some val!"
  fmt.Println(str[5:7])
}
```
```
va

```

