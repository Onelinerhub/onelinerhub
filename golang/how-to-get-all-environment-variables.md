# How to get all environment variables

```go
package main
import "os"

func main() {
  for _, env := range os.Environ() {
    print(env, "\n")
  }
}
```

- `os.Environ()` - returns list of all environment variables
- `for _, env := range os.Environ()` - iterate over all environment variables
- `import "os"` - import `os` module to work with environment variables

group: env

## Example: 
```go
package main
import "os"

func main() {
  for _, env := range os.Environ() {
    print(env, "\n")
  }
}
```
```
USER=www-data
HOME=/var/www
PWD=/tmp
```

