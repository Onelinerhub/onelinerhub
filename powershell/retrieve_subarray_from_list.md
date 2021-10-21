# How to retrieve an array that is inside another array or list

```Powershell
@("string1",'c',11,10,@(0,1,1,2,3)) | Where-Object{$_ -is [Array]}
```
- @("string1",'c',11,10,@(0,1,1,2,3)) - create an array of several data types
- Where-Object - filter list of enumerated data based on a condition
- $_ -is [Array] - retrieves the $_ iterator object for the list of data types and returns the object of type that IS [Array]


## Example

```Powershell
PS C:\Users> @("string1",'c',11,10,@(0,1,1,2,3)) | Where-Object{$_ -is [Array]}
0
1
1
2
3
PS C:\Users>
```