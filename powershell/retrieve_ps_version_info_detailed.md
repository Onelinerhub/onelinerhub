# How to get detailed PS versioning information of your system

```Powershell
"Current PS Version is {0}.{1}.{2}.{3} - Edition Mode: {4}" -f $PSVersionTable.PSVersion.Major,$PSVersionTable.PSVersion.Minor,$PSVersionTable.PSVersion.Build,$PSVersionTable.PSVersion.Revision,$PSVersionTable.PSEdition
```
- "Current PS Version is {0}.{1}.{2}.{3} - Edition Mode: {4}" - add a standard string message with 5 different string formatting placeholders provided in the order of: {0} {1} {2} {3} and {4} using a dot separator
- -f - ps switch that applies a standard string formatting option for current message placeholders on the provided variables
- $PSVersionTable.PSVersion.Major - default PS variable for powershell major version number
- $PSVersionTable.PSVersion.Minor - default PS variable for powershell minor version number
- $PSVersionTable.PSVersion.Build - default PS variable for powershell build number
- $PSVersionTable.PSVersion.Revision - default PS variable for powershell revision number
- $PSVersionTable.PSEdition - default PS variable for powershell edition type


## Example

```Powershell
PS C:\Users> "Current PS Version is {0}.{1}.{2}.{3} - Edition Mode: {4}" -f $PSVersionTable.PSVersion.Major,$PSVersionTable.PSVersion.Minor,$PSVersionTable.PSVersion.Build,$PSVersionTable.PSVersion.Revision,$PSVersionTable.PSEdition
Current PS Version is 5.1.19041.1237 - Edition Mode: Desktop
PS C:\Users>
```
