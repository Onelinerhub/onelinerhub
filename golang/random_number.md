# Generate random number

```Go
import (
    "math/rand"
    "time"
)
rand.Seed(time.Now().UnixNano())
rand.Intn(500)
```

### Explaination
```Go
// we import math/rand and time package from Go standard library
import (
    "math/rand"
    "time"
)
```

```Go
// then we pick current unix timestamp to seed `rand`, this is required else you will always get same number  because Go uses seed value of 1 by default
rand.Seed(time.Now().UnixNano())
```

- ```rand.Intn(500)``` here we pass upto a number we want to generate (500 in this case)
- if you don't care about an upper limit you can use `rand.Int()` which takes no argument
- This snippet can be useful when you want to pick a random element from an array for example
