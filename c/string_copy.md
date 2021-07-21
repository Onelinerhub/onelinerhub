# Copy one string to another

```C
#include <string.h>
strcpy(x,y);
```

- include <string.h - Name of library to be included
- strcpy(x,y) - Function to copy the string y to string x (note: x string need to have the same or greater length than y)

## Example
```C
#include <stdio.h>
#include <string.h>
int main(){
	char y[] = "Hello World!", x[13]; // Length of 13 with '\0'
	strcpy(x,y);
	printf("%s", x);
	return 0;
}
```
```bash
Hello World!
```

other_way: using a loop to copy character by character
```C
#include <stdio.h>
int main(){
	char y[] = "Hello World!", x[13]; // 13 with '\0'
	int i;
	for(i = 0; y[i] != '\0'; i++)
		x[i] = y[i];
	x[i] = '\0';
	printf("%s", x);
	return 0;
}
```
- x[i] = y[i] - Copy each caracter of string y to string x
- x[i] = '\0' - Set the last character as a terminating character
