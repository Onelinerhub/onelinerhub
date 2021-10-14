# How to select all even numbers from a list

``` C#
Enumerable.Range(1,20).Where(n => n % 2 == 0);
```
- Enumerable.Range(1,20) - get an enumerable list populated with integers from 1 to 20
- .Where - select all integers from that list where a condition is applied by an arrow function
- n => n % 2 == 0 - arrow function used to determine whether the number n tested has modulo % of zero when divided by 2