# How to sleep for 500 milliseconds

```go
package main
import "time"

func main() {
  print("Sleeping...")
  time.Sleep(500 * time.Millisecond)
  print("ok")
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `time.Sleep(` - sleep for a specified time
- `500 * time.Millisecond` - we want Go to sleep for `500` milliseconds

group: sleep

## Example: 
```go
package main
import "time"

func main() {
  print("Sleeping...")
  time.Sleep(500 * time.Millisecond)
  print("ok")
}
```
```
Sleeping...ok
```

