# How to measure command execution time

### This code first sets the `$start` variable to the current date and time using the `Get-Date` cmdlet. Then, it runs some other code. After that, it waits for 15 seconds using the `Start-Sleep` cmdlet (Only for Testing Purposes). Finally, it calculates the time difference between the current date and time and the start time, and assigns it to the `$time` variable.

```bash
$start = Get-Date;
# Other code:
Start-Sleep -Seconds 15;
$time = (Get-Date) - $start;

```
