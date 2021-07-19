# Get the length of a string

```C
#include <string.h>
strlen(x);
```

- #include <string.h> - Name of library to be included
- strlen(x) - Function to get the length of x (note: the function does not count the terminating character '\0')

## Example
```C
#include <stdio.h>
#include <string.h>
int main(){
	char x[] = "Hello World!";
	printf("%ld", strlen(x));
	return 0;
}
```
```bash
12
```

other_way: using sizeof functions (count the terminating character '\0')
```C
#include <stdio.h>
int main(){
	char x[] = "Hello World!"; // 13 with '\0'
	printf("%ld", sizeof(x) / sizeof(char));
	return 0;
}
```
- sizeof(x) / sizeof(char) - Get the size of array (x) and divided by the datatype of array (char)