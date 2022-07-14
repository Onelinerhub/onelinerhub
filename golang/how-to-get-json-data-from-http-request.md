# How to get JSON data from HTTP request

```go
package main

import ("net/http"; "io"; "encoding/json")

func main() {
  r, _ := http.Get("https://echoof.me/json")
  defer r.Body.Close()
  b, _ := io.ReadAll(r.Body)
  
  var res map[string]interface{}
  json.Unmarshal(b, &res)
  
  print(res["ip"].(string))
}
```

- `package main` - default package declaration
- `net/http` - [lib:http](https://pkg.go.dev/net/http) package to work with http protocol
- `http.Get(` - executes GET request to the specified URL
- `https://echoof.me/json` - returns request data in JSON format
- `io.ReadAll(r.Body)` - reads entire buffer (response body) into `b` bytes var
- `var res map[string]interface{}` - declare map to parse JSON with unknown structure into this variable
- `json.Unmarshal` - parses given JSON string (bytes) and saves result to `res`
- `res["ip"].(string)` - as example converts `ip` key of parsed json into string

group: http_client

## Example: 
```go
package main

import ("net/http"; "io"; "encoding/json")

func main() {
  r, _ := http.Get("https://echoof.me/json")
  defer r.Body.Close()
  b, _ := io.ReadAll(r.Body)
  
  var res map[string]interface{}
  json.Unmarshal(b, &res)
  print(res["ip"].(string))
}
```
```
135.181.98.214
```

