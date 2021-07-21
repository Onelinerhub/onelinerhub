# Get the sine and cosine of a number

```C
#include <math.h>
sin(x);
cos(x);
```

- include <math.h - Name of library to be included
- sin(x) - Function to get the sine of x in radians
- cos(x) - Function to get the cossine of x in radians

## Example
```C
#include <stdio.h>
#include <math.h>
int main(){
	double x = M_PI/4; // 45°
	printf("%.2lf %.2lf", sin(x), cos(x));
	return 0;
}
```
```bash
0.71 0.71
```
