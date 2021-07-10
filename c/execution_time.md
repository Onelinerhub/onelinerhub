# How to get the execution time of functions

```C
#include <stdlib.h>
#include <sys/time.h>
struct timeval start; gettimeofday(&start,NULL); gettimeofday(&end,NULL);
```

- struct timeval start - Declaration of the structure to collect the actual time
- gettimeofday(&start,NULL) - Collect the actual time of day (collect seconds and microsseconds)

## Example
```C
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h> // or #include <windows.h>
int main(){
	struct timeval start,end;
	gettimeofday(&start,NULL);
	sleep(2);
	gettimeofday(&end,NULL);
	printf("%ld %ld", end.tv_sec - start.tv_sec, end.tv_usec - start.tv_usec);
	return 0;
}
```
```bash
2 78
```
