# knowing better your computer

- [using PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/samples/collecting-information-about-computers?view=powershell-7.5)

```powershell
PS C:\Users\jeanp> Get-CimInstance -ClassName Win32_ComputerSystem | Select-Object -Property Model

Model
-----
HP ENVY Laptop 13-ba1xxx # Adapt for the Omnibook
```

# installing WSL using the Powershell

- Done on the Omnibook [using wsl on the Powershell](https://learn.microsoft.com/en-us/windows/wsl/install)
- To open the Window Power Shell in Administrtive Mode
  - Search for The **Window Power Shell app** on your computer
    - (Search bar in the Application menu)
  - Right click on the App Icon
    - select **Open as Administrator**
    - Accept on the Alert Box
