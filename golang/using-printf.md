# Printing with printf() example

```go
package main
import "fmt"

func main() {
  fmt.Printf("%05d", 234)
}
```

- `func main() {` - declare `main` function that will be launched automatically
- `package main` - default package declaration
- `fmt.Printf(` - prints formatted string
- `%05d` - format value as number, pad with 5 zeros
- `234` - sample value to print

group: printf

## Example: 
```go
package main
import "fmt"

func main() {
  fmt.Printf("%05d", 234)
}
```
```
00234
```

