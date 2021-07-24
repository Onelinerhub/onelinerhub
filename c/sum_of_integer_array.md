# How to find the sum of all the elements of an integer array?

```C
int sum(int arr[], int n) {
    int sum = 0;
    for (int i=0; i<n; i++)
      sum += arr[i];
    return sum;
}
```

- int arr[] - The name of the integer array of which sum is to be calculated
- int n - Number of elements in the array named arr
- for - For loop in C through which we can iterate multiple number of times


## Example
```C
#include <stdio.h>
int sum(int arr[], int n) {
    int sum = 0;
    for (int i=0; i<n; i++)
      sum += arr[i];
    return sum;
}
int main(){
	int my_array = [1, 2, 3, 4, 6, 7, 8, 9, 10];
  int number_of_elements = 9;
  printf("%d: is the sum of the given array", sum(my_array, number_of_elements));
  return 0;
}
```
```bash
50: is the sum of the given array
```
