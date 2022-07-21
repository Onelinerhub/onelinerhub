# How to sleep for 5 seconds

```go
package main
import "time"

func main() {
  print("Sleeping...")
  time.Sleep(5 * time.Second)
  print("ok")
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `time.Sleep(` - sleep for a specified time
- `5 * time.Second` - we want Go to sleep for `5` second

group: sleep

## Example: 
```go
package main
import "time"

func main() {
  print("Sleeping...")
  time.Sleep(5 * time.Second)
  print("ok")
}
```
```
Sleeping...ok
```

