# Get the power of a number

```C
#include <math.h>
pow(x,y);
```

- #include <math.h> - Name of library to be included
- pow(x,y) - Function to get x raised to the yth power (x**y)

## Example
```C
#include <stdio.h>
#include <math.h>
int main(){
	printf("%.2f", pow(2,10));
	return 0;
}
```
```bash
1024.00
```