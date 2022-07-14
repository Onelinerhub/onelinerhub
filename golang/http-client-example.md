# HTTP client example

```go
package main

import ("net/http"; "os"; "io")

func main() {
  h := http.Client{}
  r, _ := h.Get("https://echoof.me/")
  defer r.Body.Close()
  io.Copy(os.Stdout, r.Body)
}
```

- `package main` - default package declaration
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `http.Client{}` - creates new HTTP client object
- `.Get(` - sends GET request to the given URL
- `.Body` - object to access response body
- `io.Copy(os.Stdout, r.Body)` - output response body to stdout

group: http_client

## Example: 
```go
package main

import ("net/http"; "os"; "io")

func main() {
  h := http.Client{}
  r, _ := h.Get("https://echoof.me/")
  defer r.Body.Close()
  io.Copy(os.Stdout, r.Body)
}
```
```
IP:       135.181.98.214
Agent:    Go-http-client/1.1

https://echoof.me
```

