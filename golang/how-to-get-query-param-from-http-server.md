# How to get query param from HTTP server

```go
package main
import ( "fmt"; "net/http" )

func hi(w http.ResponseWriter, req *http.Request) {
  fmt.Fprintf(w, req.URL.Query().Get("test"))
}

func main() {
  http.HandleFunc("/hi", hi)
  http.ListenAndServe(":8222", nil)
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `req.URL.Query().Get(` - returns query string param value by specified name
- `"/hi", hi` - handle `/hi` request with `hi()` function
- `http.ListenAndServe` - launch HTTP server
- `8222` - port to listen HTTP server on

group: http_server

## Example: 
```go
package main
import ( "fmt"; "net/http" )

func hi(w http.ResponseWriter, req *http.Request) {
  fmt.Fprintf(w, req.URL.Query().Get("test"))
}

func main() {
  http.HandleFunc("/hi", hi)
  http.ListenAndServe(":8222", nil)
}
```
```
# returns "123" on "localhost:8222/hi?test=123" request
```

