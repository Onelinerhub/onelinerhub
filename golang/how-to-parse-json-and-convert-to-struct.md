# How to parse JSON

```go
package main
import (
  "encoding/json"
  "fmt"
)

func main() {
  json_str := `{"a":25,"b": 13,"c":45}`
  var res map[string]interface{}
  json.Unmarshal([]byte(json_str), &res)
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `json_str` - sample JSON string to parse
- `res` - map variable that will contain parsed JSON
- `json.Unmarshal` - parses given JSON string (bytes) and saves result to `res`

group: json

## Example: 
```go
package main
import (
  "encoding/json"
  "fmt"
)

func main() {
  json_str := `{"a":25,"b": 13,"c":45}`
  var res map[string]interface{}
  json.Unmarshal([]byte(json_str), &res)
  fmt.Println(res)
}
```
```
map[a:25 b:13 c:45]

```

