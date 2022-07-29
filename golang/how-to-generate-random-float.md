# How to generate random float

```go
package main
import ("math/rand"; "time")

func main() {
  rnd := rand.New( rand.NewSource(time.Now().UnixNano()) )
  num := rnd.Float64() * 2 + 10
}
```

- `package main` - default package declaration
- `"math/rand"` - lib for random numbers generation
- `rand.New` - init new random generator with given seed
- `.Float64()` - returns random float from `0` to `1` exclusively
- `2` - final generated number will start from `2`
- `10` - final generated number will end with `12`
- `num` - will contain generated float

group: random

## Example: 
```go
package main
import ("math/rand"; "time")

func main() {
  rnd := rand.New( rand.NewSource(time.Now().UnixNano()) )
  num := rnd.Float64() * 2 + 10
  print(num)
}
```
```
+1.182739e+001
```

