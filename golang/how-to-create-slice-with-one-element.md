# How to create slice with one element

```go
package main
 
func main() {
  arr := [1]string{"hello"}
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `[1]string{` - create slice of `1` element of `string` type

group: slice_create

## Example: 
```go
package main
 
func main() {
  arr := [1]string{"hello"}
  print(len(arr), "\n", arr[0])
}
```
```
1
hello
```

