# How to iterate over a slice in reverse order

```go
package main

func main() {
  arr := []int{10,15,22,34,56}
  for i := len(arr) - 1; i >= 0; i-- {
    // do something with arr[i]
  }
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `[]int{10,15,22,34,56}` - sample slice to iterate over
- `for i := len(arr) - 1; i >= 0; i--` - iterate over `arr` in reverse order, starting from last index and ending at `0`

group: range

## Example: 
```go
package main

func main() {
  arr := []int{10,15,22,34,56}
  for i := len(arr) - 1; i >= 0; i-- {
    print(arr[i], " ")
  }
}
```
```
56 34 22 15 10
```

