# How to get array length

```go
func main() {
  var arr [5]int
  l := len(arr)
}
```

- `func main() {` - declare `main` function that will be launched automatically
- `[5]int` - defines array of 5 `int` elements
- `len(arr)` - returns length of `arr` array

group: arrays

## Example: 
```go
package main
import "fmt"

func main() {
  var arr [5]int
  fmt.Println(len(arr))
}
```
```
5

```

