# Set a value to every byte of an array

```C
#include <string.h>
memset(arr,0,sizeof(type)*length);
```

- arr - Name of array
- 0 - The value (consult [ASCII table](www.theasciicode.com.ar) for more datails) which every byte of array will be attributed
- sizeof(type)*length - Space of array in bytes

## Example
```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define len 5
int main(){
	char *arr = malloc(len*sizeof(int));
	printf("%s\n", arr);
	memset(arr,49,sizeof(char)*len);
	printf("%s", arr);
	free(arr);
	return 0;
}
```
```bash

11111
```

other_way: atribute the value in a loop
```C
#include <stdio.h>
#include <stdlib.h>
#define len 5
int main(){
	char *arr = malloc(len*sizeof(char));
	int i;
	for(i = 0; i < len; i++){
		printf("%c", arr[i]);
		arr[i] = 49;
	}
	printf("\n%s", arr);
	free(arr);
	return 0;
}
```
- arr[i] = 49; - Atribute the value 1 to every byte (character) in the array