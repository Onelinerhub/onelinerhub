# How to write log to file

```go
package main
import ( "log"; "os" )

func main() {
  f, err := os.OpenFile("/tmp/log.log", os.O_RDWR | os.O_CREATE | os.O_APPEND, 0666)
  if err != nil {
    log.Fatalf("Can't open log file", err)
  }
  defer f.Close()
  
  log.SetOutput(f)
  
  log.Println("something to log")
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `os.OpenFile` - opens file handler
- `log.SetOutput(` - will write logs to specified file handler
- `log.Println(` - log sample message (will be logged to file)

group: log

## Example: 
```go
package main
import ( "log"; "os" )

func main() {
  f, err := os.OpenFile("/tmp/log.log", os.O_RDWR | os.O_CREATE | os.O_APPEND, 0666)
  if err != nil {
    log.Fatalf("Can't open log file", err)
  }
  defer f.Close()
  
  log.SetOutput(f)
  
  log.Println("something to log")
}
```
```
~# cat /tmp/log.log 
2022/07/21 11:19:43 something to log

```

