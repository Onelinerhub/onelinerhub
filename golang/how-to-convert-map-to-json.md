# How to convert map to JSON

```go
package main
import ("encoding/json")

func main() {
  mp := make(map[string]string)

  mp["name"] = "Joe"
  mp["position"] = "president"
  
  str, _ := json.Marshal(mp)
  str = string(str)
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `"encoding/json"` - lib to work with JSON
- `json.Marshal` - converts given argument to JSON
- `string(` - convert given value to string

group: map

## Example: 
```go
package main
import ("encoding/json")

func main() {
  mp := make(map[string]string)

  mp["name"] = "Joe"
  mp["position"] = "president"
  
  str, _ := json.Marshal(mp)
  print(string(str))
}
```
```
{"name":"Joe","position":"president"}
```

