# How to reverse the characters in a string

``` C#
String.Join("",("1234Simple").Select(c=>c).Reverse());
```
- String.Join("", - concatenate one or more characters in a single list or array, by using empty "" string literal separator
- .Select(c=>c) - select each and every other character in a string into an array of characters
- .Reverse() - reverse each and every one elements in an array or list