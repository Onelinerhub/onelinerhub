# How to print boolean with printf()

```go
package main
import "fmt"

func main() {
  fmt.Printf("%t", true)
}
```

- `func main() {` - declare `main` function that will be launched automatically
- `package main` - default package declaration
- `fmt.Printf(` - prints formatted string
- `%t` - will print `true` or `false` depending on input value
- `true` - sample boolean value

group: printf

## Example: 
```go
package main
import "fmt"

func main() {
  fmt.Printf("%t", true)
}
```
```
true
```

