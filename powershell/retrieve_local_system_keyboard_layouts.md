# How to get local system keyboard layout information

```Powershell
Get-ItemProperty -Path "HKCU:\Keyboard Layout\Preload"
```
- Get-ItemProperty - retrieve the property of a top-level item in the local system (directory, file, registry value)
- -Path - path option switch that includes a standard directory path
- "HKCU:\Keyboard Layout\Preload" - current user registry directory path that includes preloaded sets of OS system keyboard layout


## Example

```Powershell
PS C:\Users> Get-ItemProperty -Path "HKCU:\Keyboard Layout\Preload"


2            : 00000408
1            : 00000409
3            : 0000040c
4            : 00000809
PSPath       : Microsoft.PowerShell.Core\Registry::HKEY_CURRENT_USER\Keyboard Layout\Preload
PSParentPath : Microsoft.PowerShell.Core\Registry::HKEY_CURRENT_USER\Keyboard Layout
PSChildName  : Preload
PSDrive      : HKCU
PSProvider   : Microsoft.PowerShell.Core\Registry



PS C:\Users>
```