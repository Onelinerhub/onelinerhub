# How to use range with map

```go
package main

func main() {
  mp := map[string]string{"joe": "president", "donald": "not"}

  for k, v := range mp {
    print(k, ":", v, ";")
  }
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `map[string]string{` - creates new map
- `for k, v := range mp` - iterate over `mp` map having keys/values in `k` and `v` respectively

group: range

## Example: 
```go
package main

func main() {
  mp := map[string]string{"joe": "president", "donald": "not"}

  for k, v := range mp {
    print(k, ":", v, ";")
  }
}
```
```
joe:president;donald:not;
```

