# How to get substring from string

```go
package main
import "fmt"
func main() {
  str := "some val!"
  fmt.Println(str[5:])
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `"some val!"` - sample string
- `str[5:]` - extracts substring from position `5` and to the end of it

group: substring

## Example: 
```go
package main
import "fmt"
func main() {
  str := "some val!"
  fmt.Println(str[5:])
}
```
```
val!

```

