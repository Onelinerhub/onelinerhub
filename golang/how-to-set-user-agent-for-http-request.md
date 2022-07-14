# How to set user agent for HTTP request

```go
package main

import ("net/http"; "os"; "io")

func main() {
  client := &http.Client{}
  req, _ := http.NewRequest("GET", "https://echoof.me", nil)
  req.Header.Set("User-Agent", "super-go-client")
  r, _ := client.Do(req)
  defer r.Body.Close()
  io.Copy(os.Stdout, r.Body)
}
```

- `package main` - default package declaration
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `http.Client{}` - creates new HTTP client object
- `http.NewRequest` - creates HTTP request object
- `.Header.Set` - set custom header (can be executed multiple times)
- `User-Agent` - header allows to set user agent
- `super-go-client` - sample value for user agent to set
- `.Do(` - sends given request
- `io.Copy(os.Stdout, r.Body)` - output response body to stdout

group: http_client

## Example: 
```go
package main

import ("net/http"; "os"; "io")

func main() {
  client := &http.Client{}
  req, _ := http.NewRequest("GET", "https://echoof.me", nil)
  req.Header.Set("User-Agent", "super-go-client")
  r, _ := client.Do(req)
  defer r.Body.Close()
  io.Copy(os.Stdout, r.Body)
}
```
```
IP:                           135.181.98.214

ACCEPT_ENCODING:              gzip
USER_AGENT:                   super-go-client

https://echoof.me
```

