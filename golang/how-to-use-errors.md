# How to use errors

```go
package main
import "errors"

func test(param string) (string, error) {
  if param == "" {
    return "", errors.New("this is bad")
  }
  
  return "<" + param + ">", nil
}

func main() {
  res, err := test("")
}
```

- `package main` - default package declaration
- `import "errors"` - load lib to work with errors
- `errors.New(` - creates new error object
- `(string, error)` - our function will return string result and error

group: errors

## Example: 
```go
package main
import ( "fmt"; "errors" )

func test(param string) (string, error) {
  if param == "" {
    return "", errors.New("this is bad")
  }
  
  return "<" + param + ">", nil
}

func main() {
  res, err := test("")
  fmt.Println(err)
  
  res, err = test("tag")
  fmt.Println(res)
}
```
```
this is bad
<tag>

```

