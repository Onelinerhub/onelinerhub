# Concatenate two strings

```C
#include <string.h>
strcat(x,y);
```

- include <string.h - Name of library to be included
- strcat(x,y) - Function to concatenate the string y to string x (note: x string need to have a length equal or greater than length of x+y)

## Example
```C
#include <stdio.h>
#include <string.h>
int main(){
	char x[13] = "Hello ", y[] = "World!";
	strcat(x,y);
	printf("%s", x);
	return 0;
}
```
```bash
Hello World!
```

other_way: using a loop to concatenate character by character
```C
#include <stdio.h>
int main(){
	char x[13] = "Hello ", y[] = "World!"; // 13 with '\0'
	int i,j;
	for(i = 0, j = 0; y[j] != '\0'; i++, j++){
		while(x[i] != '\0') i++;
		x[i] = y[j];
	}
	x[i] = '\0';
	printf("%s", x);
	return 0;
}
```
- while(x[i] != '\0') i++; - Reach to terminating character of string to start concatenation
- x[i] = y[j]; - Concatenate y in x
- x[i] = '\0'; - Attribute the last character as terminating character
