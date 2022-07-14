# How to print new line with printf()

```go
package main
import "fmt"

func main() {
  fmt.Printf("%d\n%d", 12, 34)
}
```

- `func main() {` - declare `main` function that will be launched automatically
- `package main` - default package declaration
- `fmt.Printf(` - prints formatted string
- `%d` - will print numeric integer value
- `\n` - prints new line
- `12, 34` - sample values to print

group: printf

## Example: 
```go
package main
import "fmt"

func main() {
  fmt.Printf("%d\n%d", 12, 34)
}
```
```
12
34
```

