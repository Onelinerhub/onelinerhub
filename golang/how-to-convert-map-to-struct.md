# How to convert map to struct

```go
package main

type person struct {
  name string
  position string
}

func main() {
  mp := make(map[string]string)

  mp["name"] = "Joe"
  mp["position"] = "president"
  
  p := person{name: mp["name"], position: mp["position"]}
}
```

- `package main` - default package declaration
- `make(map[string]string)` - initialize map with string keys and string values
- `type person struct {` - define sample struct to copy map values to
- `p := person{` - create object of person struct type

group: map

## Example: 
```go
package main

type person struct {
  name string
  position string
}

func main() {
  mp := make(map[string]string)

  mp["name"] = "Joe"
  mp["position"] = "president"
  
  p := person{name: mp["name"], position: mp["position"]}
  print(p.name)
}
```
```
Joe
```

