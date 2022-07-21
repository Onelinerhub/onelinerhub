# How to define array

```go
package main
import "fmt"

func main() {
  var arr [5]int
  fmt.Println(arr)
}
```

- `package main` - default package declaration
- `import "fmt"` - loads `fmt` package to operate on strings (and print them)
- `func main() {` - declare `main` function that will be launched automatically
- `[5]int` - defines array of 5 `int` elements (by default all items will have `0` value)
- `arr` - variable will hold our array

group: arrays

## Example: 
```go
package main
import "fmt"

func main() {
  var arr [5]int
  fmt.Println(arr)
}
```
```
[0 0 0 0 0]

```

