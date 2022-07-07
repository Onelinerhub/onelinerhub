# How to parse JSON

```go
package main
import (
  "encoding/json"
  "fmt"
)
	
type person struct {
  Name string
  Age  int
}

func main() {
  json_str := "{"a":25,"b": 13,"c":45}"
  res := json.Unmarshal([]byte(json_str), &dat)
}
```

- `package main` - default package declaration
- `type person struct` - declare sample struct
- `func main() {` - declare `main` function that will be launched automatically
- `sample` - sample variable of `person` struct
- `json.Marshal` - converts given argument to JSON
- `res` - variable will contain JSON string 

group: json

## Example: 
```go
package main
import (
  "encoding/json"
  "fmt"
)
	
type person struct {
  Name string
  Age  int
}

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

