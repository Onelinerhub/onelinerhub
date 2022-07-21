# How to use ENUM type

```go
package main
 
const (
  North int = iota
  South
  East
  West
)

func main() {
  print(East)
}
```

- `const (` - defines enum constants 
- `int = iota` - assign int value to given constant and auto incremented value starting from `0`
- `East` - will have int value of `2`

## Example: 
```go
package main

const (
  North int = iota
  South
  East
  West
)

func main() {
  print(East)
}
```
```
2
```

