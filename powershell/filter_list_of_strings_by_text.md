# How to filter a list of strings by specific text included in string

```Powershell
@("TestAccount","MainCorporate","EnterpriseAccountTest","Tester1","Tester2") | Where-Object{$_ -ilike "*Test*"}
```
- @("TestAccount","MainCorporate","EnterpriseAccountTest","Tester1","Tester2") - create an array of preloaded strings
- Where-Object - filter list of enumerated data based on a condition
- {$_ -ilike "*Test*"} - retrieves the $_ iterator object for the list of strings and performs a case-insensitive match for text including the string Test in the middle of the string


## Example

```Powershell
PS C:\Users> @("TestAccount","MainCorporate","EnterpriseAccountTest","Tester1","Tester2") | Where-Object{$_ -ilike "*Test*"}
TestAccount
EnterpriseAccountTest
Tester1
Tester2
PS C:\Users>
```
