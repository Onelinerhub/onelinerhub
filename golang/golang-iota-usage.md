# How to use iota for constants

```go
package main
import "fmt"

const (
  Joe int = iota
  Donald
)

func main() {
  fmt.Println(Joe)
  fmt.Println(Donald)
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `const (` - defines constants
- `int = iota` - assign int value to given constant and auto incremented value starting from `0`
- `Joe` - first constant with value `0`
- `Donald` - second constant with value `1`

group: iota

## Example: 
```go
package main
import "fmt"

const (
  Joe int = iota
  Donald
)

func main() {
  fmt.Println(Joe)
  fmt.Println(Donald)
}
```
```
0
1

```

