# How to use if multiple (AND) conditions COPY

```go
package main

func main() {
  x := 5
  if x < 10 && x == 5 {
    print("here")
  } else {
    print("there")
  }
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `if` - start if block with condition to check
- `&&` - `and` operator to check multiple `if` conditions

group: ifelse

## Example: 
```go
package main

func main() {
  x := 5
  if x < 10 && x == 5 {
    print("here")
  } else {
    print("there")
  }
}
```
```
here
```

