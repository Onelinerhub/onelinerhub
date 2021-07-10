# Conditional using ternary operator

```C
Condition ? Then : Else;
```

- ? - Indicates the next block of code to execute if the condition is satisfied
- : - Indicates the next block of code to execute if the condition is not satisfied

## Example
```C
int x = 10;
x % 2 == 0 ? printf("Even") : printf("Odd");
```
```bash
Even
```

other_way: Standard if/else way
```C
int x = 10;
if(x % 2 == 0)
	printf("Even");
else
	printf("Odd");
```
- if(x % 2 == 0) - Indicates a condition to be satisfied: if the number is even
- else - Indicates what do to if the condition is not satisfied
