# Generate a random number

```C
#include <stdlib.h>
#include <time.h>
srand(time(NULL)); int x = rand() % 100;
```

- srand(time(NULL)) - Set the seed of rand function to generate the random number from the actual time of system
- int x = rand() % 100 - Generate a random number between 0 and 99
