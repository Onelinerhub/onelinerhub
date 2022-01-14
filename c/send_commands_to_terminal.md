# Sending commands to the terminal in a console application

```C
#include <stdlib.h>

int main(){
    system("echo foo");
    return 0;
}

```

- include <stdlib.h> - Standard C library that contains system functions
- system(arguments) - The function receives the argument and executes it on the terminal.

