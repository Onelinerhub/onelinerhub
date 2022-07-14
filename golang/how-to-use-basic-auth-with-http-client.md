# How to use basic auth with HTTP client

```go
package main

import ("net/http"; "os"; "io")

func main() {
  h := http.Client{}
  req, _ := http.NewRequest("GET", "https://echoof.me/", nil)
  req.SetBasicAuth("user", "pwd")
  r, _ := h.Do(req)
  defer r.Body.Close()
  io.Copy(os.Stdout, r.Body)
}
```

- `package main` - default package declaration
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `http.Client{}` - creates new HTTP client object
- `http.NewRequest` - creates HTTP request object
- `"GET"` - HTTP method to use
- `SetBasicAuth(` - set basic auth username and password
- `.Do(` - sends given request
- `io.Copy(os.Stdout, r.Body)` - output response body to stdout

group: http_client

## Example: 
```go
package main

import ("net/http"; "os"; "io")

func main() {
  h := http.Client{}
  req, _ := http.NewRequest("GET", "https://echoof.me/", nil)
  req.SetBasicAuth("user", "pwd")
  r, _ := h.Do(req)
  defer r.Body.Close()
  io.Copy(os.Stdout, r.Body)
}
```
```
IP:                           135.181.98.214

ACCEPT_ENCODING:              gzip
AUTHORIZATION:                Basic dXNlcjpwd2Q=
USER_AGENT:                   Go-http-client/1.1

https://echoof.me
```

