# How to use proxy with HTTP client

```go
package main

import ("net/http"; "os"; "io"; "net/url")

func main() {
  proxy, _ := url.Parse("http://host:port")
  h := &http.Client{Transport: &http.Transport{Proxy: http.ProxyURL(proxy)}}
  r,_ := h.Get("https://echoof.me");
  defer r.Body.Close()
  io.Copy(os.Stdout, r.Body)
}
```

- `package main` - default package declaration
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `http.Client{` - creates new HTTP client object
- `Transport` - specifies transport object (defines advanced request options)
- `Proxy:` - sets proxy for transport
- `http://host:port` - our proxy host and port
- `.Get(` - sends GET request to the given URL
- `io.Copy(os.Stdout, r.Body)` - output response body to stdout

group: http_client

## Example: 
```go
package main

import ("net/http"; "os"; "io"; "net/url")

func main() {
  proxy, _ := url.Parse("http://host:port")
  h := &http.Client{Transport: &http.Transport{Proxy: http.ProxyURL(proxy)}}
  r,_ := h.Get("https://echoof.me");
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

