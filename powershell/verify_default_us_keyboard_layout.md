# How to validate default keyboard layout is EN-US

```Powershell
((Get-ItemProperty -Path "HKCU:\Keyboard Layout\Preload").1 -eq "00000409")
```
- Get-ItemProperty - retrieve the property of a top-level item in the local system (directory, file, registry value)
- -Path - path option switch that includes a standard directory path
- "HKCU:\Keyboard Layout\Preload" - current user registry directory path that includes preloaded sets of OS system keyboard layout
- .1 -eq "00000409" - boolean check that registry key named 1 from the retrieve sets of keyboard layouts has value equal to 00000409


## Example

```Powershell
PS C:\Users> ((Get-ItemProperty -Path "HKCU:\Keyboard Layout\Preload").1 -eq "00000409")
True
PS C:\Users>
```