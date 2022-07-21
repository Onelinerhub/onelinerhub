# How to set environment variable

```go
package main
import "os"

func main() {
  os.Setenv("MY", "12345")
  print( os.Getenv("MY") )
}
```

- `import "os"` - import `os` module to work with environment variables
- `os.Setenv(` - sets given environment variable
- `MY` - name of environment variable to set value of
- `12345` - sample value to set

group: env

## Example: 
```go
package main
import "os"

func main() {
  os.Setenv("MY", "12345")
  print( os.Getenv("MY") )
}
```
```
12345
```

