# How to parse JSON and convert to struct

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
  json.Unmarshal([]byte(json_str), &res)
  fmt.Println(res)
}
```
```

# command-line-arguments
./test.go:13:18: syntax error: unexpected a at end of statement
```

