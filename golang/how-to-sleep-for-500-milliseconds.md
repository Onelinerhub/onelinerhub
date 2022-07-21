# How to sleep for 1 minute

```go
package main
import "time"

func main() {
  print("Sleeping...")
  time.Sleep(1 * time.Minute)
  print("ok")
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `time.Sleep(` - sleep for a specified time
- `1 * time.Minute` - we want Go to sleep for `1` minute

group: sleep

## Example: 
```go
package main
import "time"

func main() {
  print("Sleeping...")
  time.Sleep(1 * time.Minute)
  print("ok")
}
```
```
Sleeping...ok
```

