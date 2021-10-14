# How to determine length of a list is even

``` C#
(Enumerable.Range(1,20).Count() % 2 == 0)
```
- Enumerable.Range(1,20) - get an enumerable list populated with integers from 1 to 20
- .Count() - retrieve the total length of the list as a number
- % 2 == 0 - check whether a number has modulo % of zero when divided by 2