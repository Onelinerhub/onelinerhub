# How to wrap error

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

- `package main` - default package declaration
- `import "errors"` - load lib to work with errors
- `get_error` - sample function that returns error
- `errors.New(":(")` - create new error object
- `fmt.Errorf(` - wraps given error object with additional message using `%w` symbol

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

