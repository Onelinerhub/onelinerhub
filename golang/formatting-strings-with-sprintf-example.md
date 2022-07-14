# Formatting strings with Sprintf() example

```go
package main
import "fmt"

func main() {
  print(fmt.Sprintf("%05d", 234))
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `fmt.Sprintf(` - formats given string based on a given template and return result

group: printf

## Example: 
```go
package main
import "fmt"

func main() {
  print(fmt.Sprintf("%05d", 234))
}
```
```
00234
```

