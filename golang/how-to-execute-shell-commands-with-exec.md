# How to execute shell commands with exec()

```go
package main

import ( "os/exec"; "fmt"; "bytes" )

func main() {
  cmd := exec.Command("/usr/bin/du", "-sh", "/tmp")
  
  var out bytes.Buffer
  cmd.Stdout = &out
  
  cmd.Run()
  fmt.Printf(out.String())
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `exec.Command(` - creates shell command executable object
- `/usr/bin/du` - command to execute
- `"-sh", "/tmp"` - commands options (each option is separate argument, can have any number of them)
- `cmd.Stdout = &out` - ask Go to return command output to `out` variable
- `cmd.Run()` - execute prepared command
- `out.String()` - converts output bytes Buffer to string

## Example: 
```go
package main

import ( "os/exec"; "fmt"; "bytes" )

func main() {
  cmd := exec.Command("/usr/bin/du", "-sh", "/tmp")
  
  var out bytes.Buffer
  cmd.Stdout = &out
  
  cmd.Run()
  fmt.Printf(out.String())
}
```
```
5.7M	/tmp

```

