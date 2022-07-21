# How to log panic

### Errors can be logged as simply as:

```go
package main
import "log"

func main() {
  log.Panic("oh no no no")
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `log.Panic(` - will log message and call `panic()` after that

group: log

## Example: 
```go
package main
import "log"

func main() {
  log.Panic("oh no no no")
}
```
```
2022/07/21 11:32:59 oh no no no
panic: oh no no no

goroutine 1 [running]:
log.Panic({0xc000108f60?, 0x0?, 0x492800?})
	/usr/lib/go-1.18/src/log/log.go:385 +0x65
main.main()
	/tmp/test.go:5 +0x45
exit status 2
```

