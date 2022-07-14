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
  
  p := person{}
  
  vals := make([]string, 0, len(mp))
  for  _, v := range mp {
     vals = append(vals, v)
  }
}
```

- `package main` - default package declaration
- `make(map[string]string)` - initialize map with string keys and string values
- `len(` - returns length of a given map
- `vals = append(vals, v)` - add each `mp` value to `vals` slice

group: map

```
# command-line-arguments
./test.go:20:20: undefined: reflect
```

