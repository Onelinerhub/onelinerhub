# Unrmarshal example

```go
package main
import "encoding/json"

type President struct {
  Name string
  Age int
}

func main() {
  s := `{"Name":"Joe","Age":99}`
  p := President{}
  json.Unmarshal([]byte(s), &p)
}
```

- `package main` - default package declaration
- `"encoding/json"` - lib to work with JSON
- `type President struct` - defines struct with fields
- `President` - struct name
- `{"Name":"Joe","Age":99}` - sample json string to unmarshal into `struct`
- `p := President{}` - this variable will store unmarshalled data

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
  s := `{"Name":"Joe","Age":99}`
  p := President{}
  json.Unmarshal([]byte(s), &p)
  
  print(p.Name, ": ", p.Age)
}
```
```
Joe: 99
```

