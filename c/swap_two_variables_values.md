# Swapping two variables values using the logical operator XOR

```C
int x = 2, y = 3; x = x ^ y; y = x ^ y; x = x ^ y;
```

- int x = 2, y = 3 - Declaration of variables
- x = x ^ y - Perform the XOR operation (note: equal numbers in XOR have 0 as result) to manipulate the value of y
- y = x ^ y - Attribute the initial value of x to y
- x = x ^ y - Attribute the initial value of y to x
