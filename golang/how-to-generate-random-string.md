# How to generate random string

### This solution is based on [Paul Hankins' code](https://stackoverflow.com/questions/22892120/how-to-generate-a-random-string-of-a-fixed-length-in-go/22892986#22892986).

```go
package main
import ( "time"; "math/rand" )

var letters = []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

func rand_str(n int) string {
  b := make([]rune, n)
  for i := range b {
    b[i] = letters[rand.Intn(len(letters))]
  }
  return string(b)
}

func main() {
  rand.Seed(time.Now().UnixNano())
  res := rand_str(30)
}
```

- `package main` - default package declaration
- `"math/rand"` - lib for random numbers generation
- `rand.New` - init new random generator with given seed
- `rand.Seed(` - init random generator with new seed
- `rand_str(` - custom function that returns random string of a given length
- `make([]rune, n)` - makes a map of a `n` elements
- `for i := range b {` - iterate all `b` (map) elements
- `letters[rand.Intn(len(letters))]` - populate each `b` element with random elements from `letters` array

group: random

## Example: 
```go
package main
import ( "time"; "math/rand" )

var letters = []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

func rand_str(n int) string {
  b := make([]rune, n)
  for i := range b {
    b[i] = letters[rand.Intn(len(letters))]
  }
  return string(b)
}

func main() {
  rand.Seed(time.Now().UnixNano())
  res := rand_str(30)
  print(res)
}
```
```
iiSohqBecttbFDXygjOKhvzFxPabFd
```

