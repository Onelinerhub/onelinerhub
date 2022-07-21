# How to log fatal error

### Errors can be logged as simply as:

```go
package main
import "log"

func main() {
  log.Fatal("oh no")
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `log.Fatal(` - will log message and call `os.Exit(1)` after that

group: log

## Example: 
```go
package main
import "log"

func main() {
  log.Fatal("oh no")
}
```
```
2022/07/21 11:31:59 oh no
exit status 1
```

