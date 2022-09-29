# How to use ipcalc with IP address

```txt
ipcalc 8.8.8.8
```

- `ipcalc` - perform simple manipulation of IP addresses
- `8.8.8.8` - example IP address to use

group: ipcalc

## Example: 
```txt
ipcalc 8.8.8.8
```
```
Address:   8.8.8.8              00001000.00001000.00001000. 00001000
Netmask:   255.255.255.0 = 24   11111111.11111111.11111111. 00000000
Wildcard:  0.0.0.255            00000000.00000000.00000000. 11111111
=>
Network:   8.8.8.0/24           00001000.00001000.00001000. 00000000
HostMin:   8.8.8.1              00001000.00001000.00001000. 00000001
HostMax:   8.8.8.254            00001000.00001000.00001000. 11111110
Broadcast: 8.8.8.255            00001000.00001000.00001000. 11111111
Hosts/Net: 254                   Class A
```

