# How to retrieve numbers divisible by 10 from a list of values

```Powershell
1..100 | Where-Object{$_ % 10 -eq 0}
```
- 1..100 - create a numeric sequence from 1 to 100
- Where-Object - filter list of enumerated data based on a condition
- {$_ % 10 -eq 0} - retrieves the $_ iterator object for the list of numeric values such that value modulo % 10 equals to zero


## Example

```Powershell
PS C:\Users> 1..100 | Where-Object{$_ % 10 -eq 0}
10
20
30
40
50
60
70
80
90
100
PS C:\Users>
```
