# Get the round of a float number

```C
#include <math.h>
round(x);
floor(x);
ceil(x);
```

- include <math.h - Name of library to be included
- round(x); - Function to get the x rounded
- floor(x); - Function to get the x rounded to a lower value
- ceil(x); - Function to get the x rounded to a greater value

## Example
```C
#include <stdio.h>
#include <math.h>
int main(){
	double x = 2.5;
	printf("%.2lf %.2lf %.2lf", round(x), floor(x), ceil(x));
	return 0;
}
```
```bash
3.00 2.00 3.00
```
