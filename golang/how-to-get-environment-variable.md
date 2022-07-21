# How to get environment variable

```go
package main
import "os"

func main() {
  print( os.Getenv("PWD") )
}
```

- `import "os"` - import `os` module to work with environment variables
- `os.Getenv(` - returns value for a given environment variable
- `PWD` - name of environment variable to get value of

group: env

## Example: 
```go
package main
import "os"

func main() {
  print( os.Getenv("PWD") )
}
```
```
/tmp
```

