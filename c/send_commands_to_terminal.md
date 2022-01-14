# Sending commands to the terminal in a console application

```c
#include <stdlib.h>

int main(){
    system("echo foo");
    return 0;
}
```

- `include <stdlib.h>` - standard C library that contains system functions
- `system("echo foo")` - function receives the argument (`echo foo` in this case) and executes it on the terminal.


