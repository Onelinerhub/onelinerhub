# Iterate through map ("foreach" style)

```go
package main
import "fmt"

func main() {
  mp := make(map[string]int)
  mp["a"] = 1
  mp["b"] = 2
  
  for k, v := range mp {
    fmt.Println(k, v)
  }
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `mp := make(map[string]int)` - create sample map
- `for k, v := range mp` - iterate through `map` map with keys accessible via `k` and value via `v`

group: for

## Example: 
```go
package main
import "fmt"

func main() {
  mp := make(map[string]int)
  mp["a"] = 1
  mp["b"] = 2
  
  for k, v := range mp {
    fmt.Println(k, v)
  }
}
```
```
a 1
b 2

```

