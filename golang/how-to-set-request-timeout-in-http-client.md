# How to set request timeout in HTTP client

```go
package main

import ("net/http"; "os"; "io"; "time")

func main() {
  h := http.Client{Timeout: 3 * time.Second}
  r, _ := h.Get("https://echoof.me/")
  defer r.Body.Close()
  io.Copy(os.Stdout, r.Body)
}
```

- `package main` - default package declaration
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `http.Client{` - creates HTTP client object
- `Timeout:` - sets request timeout
- `3 * time.Second` - timeout is set to `3` seconds
- `.Body` - object to access response body
- `io.Copy(os.Stdout, r.Body)` - output response body to stdout

group: http_client

## Example: 
```go
package main

import ("net/http"; "os"; "io"; "time")

func main() {
  h := http.Client{Timeout: 3 * time.Second}
  r, _ := h.Get("https://echoof.me/")
  defer r.Body.Close()
  io.Copy(os.Stdout, r.Body)
}
```
```
IP:                           135.181.98.214

ACCEPT_ENCODING:              gzip
USER_AGENT:                   Go-http-client/1.1

https://echoof.me
```

