# How to parse JSON and convert to struct

```go
package main
import (
  "encoding/json"
  "fmt"
)

type data struct {
  A int
  B int
}

func main() {
  json_str := `{"A":25,"B":13}`
  var res data
  json.Unmarshal([]byte(json_str), &res)
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `json_str` - sample JSON string to parse
- `res` - variable of `data` struct type
- `json.Unmarshal` - parses given JSON string (bytes) and saves result to `res`

group: json

## Example: 
```go
package main
import (
  "encoding/json"
  "fmt"
)

type data struct {
  A int
  B int
}

func main() {
  json_str := `{"A":25,"B":13}`
  var res data
  json.Unmarshal([]byte(json_str), &res)
  
  fmt.Println(res)
}
```
```
{25 13}

```

