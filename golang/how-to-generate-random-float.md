# How to generate random float

```go
package main
import ("math/rand"; "time")

func main() {
  rnd := rand.New( rand.NewSource(time.Now().UnixNano()) )
  num := rnd.Intn(25)
}
```

- `package main` - default package declaration
- `"math/rand"` - lib for random numbers generation
- `rand.New` - init new random generator with given seed
- `.Intn(` - returns random number from `0` to the given number (`25` in our case)
- `num` - will contain random int

group: random

## Example: 
```go
package main
import ("math/rand"; "time")

func main() {
  rnd := rand.New( rand.NewSource(time.Now().UnixNano()) )
  num := rnd.Intn(25)
  print(num)
}
```
```
16
```

