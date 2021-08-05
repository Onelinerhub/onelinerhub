# Copy a string to another

instead of using the <string.h> which will make the output way bigger you could just use this piece of code:

```c
char *temp=a;while (*temp++ = *b++);
```

## Example

```c
#include <stdio.h>
int main() {
    char a[6], *b = "test\n\0";
    char *temp=a;while (*temp++ = *b++);
    printf("%s", a);
    return 0;
}
```
```
test
```
