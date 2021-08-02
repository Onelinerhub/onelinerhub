# Swapping two variables values using the logical operator XOR

Note: equal numbers in XOR (`^`) have 0 as result

```C
x ^= y ^= x ^= y;
```

- x ^= y; - Perform the XOR operation between `x`and `y`. Store the value in `x`.
- y ^= - Perform the XOR operation between the XOR-ed value of `x` and `y`. Store the value in `y` (it's now the original `x`).
- x ^= - Perform the XOR operation between the XOR-ed value of `y` and `x`. Store the value in `x` (it's now the original `y`).

## Example
```c
int x = 2;
int y = 3;

// Swap the values
x ^= y ^= x ^= y;
```
