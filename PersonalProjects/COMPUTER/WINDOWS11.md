# knowing better your computer
* [using PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/samples/collecting-information-about-computers?view=powershell-7.5)
```powershell
PS C:\Users\jeanp> Get-CimInstance -ClassName Win32_ComputerSystem | Select-Object -Property Model

Model
-----
HP ENVY Laptop 13-ba1xxx
```