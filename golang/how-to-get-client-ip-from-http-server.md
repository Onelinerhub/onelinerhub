# How to get client IP from HTTP server

```go
package main
import ( "fmt"; "net/http"; "strings" )

func ip(w http.ResponseWriter, req *http.Request) {
  fmt.Fprintf(w, strings.Split(req.RemoteAddr, ":")[0])
}

func main() {
  http.HandleFunc("/ip", ip)
  http.ListenAndServe(":8222", nil)
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `strings.Split(req.RemoteAddr, ":")` - extract `IP` from client `IP:PORT` string
- `"/ip", ip` - handle `/ip` request with `ip()` function
- `http.ListenAndServe` - launch HTTP server
- `8222` - port to listen HTTP server on

group: http_server

## Example: 
```go
package main
import ( "fmt"; "net/http"; "strings" )

func ip(w http.ResponseWriter, req *http.Request) {
  fmt.Fprintf(w, strings.Split(req.RemoteAddr, ":")[0])
}

func main() {
  http.HandleFunc("/ip", ip)
  http.ListenAndServe(":8222", nil)
}
```
```
# returns [ip] on "localhost:8222/hi" request
```

