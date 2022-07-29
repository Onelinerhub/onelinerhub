# Marshal example

```go
package main
import "encoding/json"

type President struct {
  Name string
  Age int
}

func main() {
  p := President{Name: "Joe", Age: 99}
  res, _ := json.Marshal(p)
}
```

- `package main` - default package declaration
- `"encoding/json"` - lib to work with JSON
- `type President struct` - defines struct with fields
- `President` - struct name
- `json.Marshal` - converts given variable (`President` struct in our case) to JSON

group: marshal

## Example: 
```go
package main
import "encoding/json"

type President struct {
  Name string
  Age int
}

func main() {
  p := President{Name: "Joe", Age: 99}
  res, _ := json.Marshal(p)
  print(string(res))
}
```
```
{"Name":"Joe","Age":99}
```

