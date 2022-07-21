# How to unwrap error

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
  wrapped_err := get_error(true)
  fmt.Println(errors.Unwrap(wrapped_err))
}
```

- `package main` - default package declaration
- `import "errors"` - load lib to work with errors
- `get_error` - sample function that returns error
- `errors.New(":(")` - create new error object
- `fmt.Errorf(` - wraps given error object with additional message using `%w` symbol
- `errors.Unwrap(` - unwraps given wrapped error to original error (or `nil` if it's not wrapped error)

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
  wrapped_err := get_error(true)
  fmt.Println(errors.Unwrap(wrapped_err))
}
```
```
:(

```

