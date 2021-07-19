# Get the square root of a number

```C
#include <math.h>
sqrt(x);
```

- #include <math.h> - Name of library to be included
- sqrt(x) - Function to get the square root of x

## Example
```C
#include <stdio.h>
#include <math.h>
int main(){
	printf("%.2f", sqrt(81));
	return 0;
}
```
```bash
9.00
```

other_way: using pow function
```C
#include <stdio.h>
#include <math.h>
int main(){
	printf("%.2f", pow(81,0.5));
	return 0;
}
```
- pow(81,0.5) - 81 raised to the 0.5 power (square root)