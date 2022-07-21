# How to declare array of strings

```go
func main() {
  arr := [5]string{"a","b","c","d","e"}
}
```

- `func main() {` - declare `main` function that will be launched automatically
- `[5]string` - defines array of 5 `string` elements
- `{"a","b","c","d","e"}` - list of values new array will have

group: arrays

## Example: 
```go
package main
import "fmt"

func main() {
  arr := [5]string{"a", "b", "c", "d", "e"}
  fmt.Println(arr)
}
```
```
[a b c d e]

```

