# How to log errors

### Errors can be logged as simply as:

```go
package main
import ( "log"; "errors" )

func main() {
  log.Println(errors.New("oops"))
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `log.Println(` - write given message to log
- `errors.New(` - creates new error object

group: log

## Example: 
```go
package main
import ( "log"; "errors" )

func main() {
  log.Println(errors.New("oops"))
}
```
```
2022/07/21 11:24:49 oops
```

