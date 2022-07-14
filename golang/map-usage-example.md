# Map usage example

```go
package main
import "fmt"

func main() {
  mp := make(map[string]string)

  mp["name"] = "Joe"
  mp["position"] = "president"
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `make(map[string]string)` - initialize map with string keys and string values
- `mp["name"]` - set value of `name` key

group: map

## Example: 
```go
package main
import "fmt"

func main() {
  mp := make(map[string]string)

  mp["name"] = "Joe"
  mp["position"] = "president"

  fmt.Println(mp)
}
```
```
map[name:Joe position:president]

```

