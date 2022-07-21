# How to declare custom array

```go
func main() {
  arr := [5]int{10,12,50,400,8}
}
```

- `func main() {` - declare `main` function that will be launched automatically
- `[5]int` - defines array of 5 `int` elements
- `{10,12,50,400,8}` - list of values new array will have

group: arrays

## Example: 
```go
package main
import "fmt"

func main() {
  arr := [5]int{10,12,50,400,8}
  fmt.Println(arr)
}
```
```
[10 12 50 400 8]

```

