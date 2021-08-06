# Copy a string to another

Instead of using the <string.h> which will make the output way bigger you could just use this piece of code:

```c
char *temp=a;while(*temp++=*b++);
```

- `char *temp=a;` - create a temporary pointer to the initial string
- `(*temp++=*b++);` - make the first element of `temp` the first element of `b` and shift them both by one 
- `while(` - take the returned value (which is the current element of `b`) and if it's not `'\0'` continue

## Example

```c
#include <stdio.h>
int main() {
    char a[6], *b = "test\n\0";
    char *temp=a;while(*temp++=*b++);
    printf("%s", a);
    return 0;
}
```
```
test
```
