# How to wrap error

```go
package main
import "errors"

func get_error(really bool) (error) {
  if really {
    return errors.New(":(")
  }
  
  return nil
}

func main() {
  err := get_error(true)
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
import "errors"
import "fmt"

func get_error(really bool) (error) {
  e := errors.New(":(")
  if really {
    return fmt.Errorf("Hmm: %w", e)
  }
  
  return nil
}

func main() {
  err := get_error(true)
  fmt.Println(err)
}
```
```
Hmm: :(

```

