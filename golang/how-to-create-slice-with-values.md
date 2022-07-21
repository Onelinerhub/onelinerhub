# How to create slice with values

```go
package main
 
func main() {
  arr := [3]int{3,6,8}
  print(arr[1])
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `[3]int{3,6,8}` - create slice of `3` elements of `int` type with given values

group: slice_create

## Example: 
```go
package main
 
func main() {
  arr := [3]int{3,6,8}
  print(arr[1])
}
```
```
6
```

