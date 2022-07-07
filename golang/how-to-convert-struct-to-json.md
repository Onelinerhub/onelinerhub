# How to convert struct to JSON

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
  sample := &person{Name: "Joe", Age: 90}
  res, _ := json.Marshal(sample)
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
  sample := &person{Name: "Joe", Age: 90}
  res, _ := json.Marshal(sample)
  fmt.Println(string(res))
}
```
```
{"Name":"Joe","Age":90}

```

