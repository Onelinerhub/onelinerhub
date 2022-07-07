# Iterate through struct ("foreach" style)

```go
package main
import "fmt"
import "reflect"

func main() {
  st := struct{name string; age int }{"Joe", 25}
  v := reflect.ValueOf(st)

  for i := 0; i < v.NumField(); i++ {
    fmt.Println(i, v.Field(i))
  }
}
```

- `package main` - default package declaration
- `st` - sample structure
- `reflect.ValueOf(st)` - returns reflection for given structure
- `for i := 0; i < v.NumField(); i++` - iterate over all values of structure

group: for

## Example: 
```go
package main
import "fmt"
import "reflect"

func main() {
  st := struct{name string; age int }{"Joe", 25}
  v := reflect.ValueOf(st)

  for i := 0; i < v.NumField(); i++ {
    fmt.Println(i, v.Field(i))
  }
}
```
```
0 Joe
1 25

```

