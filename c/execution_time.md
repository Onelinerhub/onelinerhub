# How to get the execution time of functions

```C
#include <time.h>
clock_t tic, toc; tic = clock(); /*Some code*/ toc = clock();
```
- clock_t - variable to get the clock time
- clock() - function that gets the clock time

## Example
```C
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
	clock_t tic, toc;
	tic = clock();
	sleep(2);
	toc = clock();
	printf("sec %lu usec %lu", (unsigned long)(toc-tic) / CLOCKS_PER_SEC, (unsigned long)(toc-tic) % 1000000);
	return 0;
}
```
```bash
2 78
```

alternative_tech: gettimeofday function
```C
#include <stdlib.h>
#include <sys/time.h>
struct timeval start; gettimeofday(&start,NULL); gettimeofday(&end,NULL);
```

- struct timeval start - Declaration of the structure to collect the actual time
- gettimeofday(&start,NULL) - Collect the actual time of day (collect seconds and microsseconds)
