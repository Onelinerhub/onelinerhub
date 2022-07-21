# How to append value to array

```go
func main() {
  var arr []string
  arr = append(arr, "a", "b")
  arr = append(arr, "c")
  fmt.Println(arr)
}
```

- `func main() {` - declare `main` function that will be launched automatically
- `var arr []string` - declare sample string slice
- `append` - appends given value(s) to specified slice
- `arr` - slice to append values to
- `"a", "b"` - you can append multiple values at once
- `"c"` - or single value

group: arrays

## Example: 
```go
package main
import "fmt"

func main() {
  var arr []string
  arr = append(arr, "a", "b")
  arr = append(arr, "c")
  fmt.Println(arr)
}
```
```
[a b c]

```

