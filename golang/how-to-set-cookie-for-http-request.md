# How to set cookie for HTTP request

```go
package main

import ("net/http"; "os"; "io")

func main() {
  client := &http.Client{}
  req, _ := http.NewRequest("GET", "https://echoof.me", nil)
  req.AddCookie(&http.Cookie{
    Name: "mycookie", Value: "hi", MaxAge: 60,
  })
  r, _ := client.Do(req)
  defer r.Body.Close()
  io.Copy(os.Stdout, r.Body)
}
```

- `package main` - default package declaration
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `http.Client{}` - creates new HTTP client object
- `http.NewRequest` - creates HTTP request object
- `.AddCookie(` - adds given cookie to request
- `http.Cookie` - cookie object with params
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
  req.AddCookie(&http.Cookie{
    Name: "mycookie",
    Value: "hi",
    MaxAge: 60,
  })
  r, _ := client.Do(req)
  defer r.Body.Close()
  io.Copy(os.Stdout, r.Body)
}
```
```
IP:                           135.181.98.214

ACCEPT_ENCODING:              gzip
COOKIE:                       mycook=hi
USER_AGENT:                   Go-http-client/1.1

https://echoof.me
```

