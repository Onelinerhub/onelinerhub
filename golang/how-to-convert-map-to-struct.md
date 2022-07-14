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

## Example: 
```go
package main

import "reflect";

type person struct {
  name string
  position string
}

func main() {
  mp := make(map[string]string)

  mp["name"] = "Joe"
  mp["position"] = "president"
  
  p := person{}
  
  for  k, v := range mp {
    structValue := reflect.ValueOf(p).Elem()
    structFieldValue := structValue.FieldByName(k)
    structFieldValue.Set(reflect.ValueOf(&v))
  }
  
  print(p.name)
}
```
```
panic: reflect: call of reflect.Value.Elem on struct Value

goroutine 1 [running]:
reflect.Value.Elem({0x476480?, 0xc000048020?, 0x47fcce?})
	/usr/lib/go-1.18/src/reflect/value.go:1213 +0x1a5
main.main()
	/tmp/test.go:19 +0x28a
exit status 2
```

