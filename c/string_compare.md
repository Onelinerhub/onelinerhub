# Check if both strings are equal

```C
#include <string.h>
strcmp(x,y);
```

- #include <string.h> - Name of library to be included
- strcmp(x,y) - Function to compare if both strings are equal. Returning 0 if so, a number greater than 0 if x is greater than y and a number lower than 0 if y is greater than x

## Example
```C
#include <stdio.h>
#include <string.h>
int main(){
	char x[] = "Hello World!";
	char y[] = "Onelinerhub";
	printf("%d", strcmp(x,y));
	return 0;
}
```
```bash
-7
```
