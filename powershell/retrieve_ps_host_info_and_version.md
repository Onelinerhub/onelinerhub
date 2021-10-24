# How to get current PS cmdlet general shell hosting info and version(s)

```Powershell
"Current PS Host is {0}, of Instance {1} LANG: {2}" -f $Host.Version, $Host.InstanceId, $Host.CurrentCulture
```
- "Current PS Host is {0}, of Instance {1} LANG: {2}" - add a standard string message with 3 different string formatting placeholders provided in the order of: {0} {1} and {2}
- -f - ps switch that applies a standard string formatting option for current message placeholders on the provided variables
- $Host.Version - default PS variable for cmdlet shell hosting version number
- $Host.InstanceId - default PS variable for cmdlet shell hosting instance Id
- $Host.CurrentCulture - default PS variable for cmdlet shell hosting language culture code