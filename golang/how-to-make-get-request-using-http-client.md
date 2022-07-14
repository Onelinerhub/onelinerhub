# How to make GET request using HTTP client

```go
package main

import ("net/http"; "os"; "io")

func main() {
  r, _ := http.Get("https://echoof.me")
  defer r.Body.Close()
  io.Copy(os.Stdout, r.Body)
}
```

- `package main` - default package declaration
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `http.Get(` - executes GET request to the specified URL
- `io.Copy(os.Stdout, r.Body)` - output response body to stdout

group: http_client

## Example: 
```go
package main

import ("net/http"; "os"; "io")

func main() {
  r, _ := http.Get("https://echoof.me")
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

