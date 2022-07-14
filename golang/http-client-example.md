# HTTP client example

```go
package main

func main() {
  print("hi")
}
```


group: http_client

## Example: 
```go
package main

import "net/http"

func main() {
  h := http.Client{}
  r, _ := h.Get("https://onelinerhub.com/")
  defer r.Body.close()
  print(r.Body)
}
```
```
# command-line-arguments
./test.go:6:8: missing argument in conversion to http.Client
```

