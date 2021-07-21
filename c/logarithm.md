# Get the logarithm of a number (base-10)

```C
#include <math.h>
log10(x);
```

- include <math.h - Name of library to be included
- log10(x) - Function to get the logarithm of x

## Example
```C
#include <stdio.h>
#include <math.h>
int main(){
	printf("%.2f", log10(1000));
	return 0;
}
```
```bash
3.00
```
