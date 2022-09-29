# How to use ipcalc with netmask

```txt
ipcalc 10.0.0.0/16
```

- `ipcalc` - perform simple manipulation of IP addresses
- `10.0.0.0/16` - example netmask to use

group: ipcalc

## Example: 
```txt
ipcalc 10.0.0.0/16
```
```
Address:   10.0.0.0             00001010.00000000. 00000000.00000000
Netmask:   255.255.0.0 = 16     11111111.11111111. 00000000.00000000
Wildcard:  0.0.255.255          00000000.00000000. 11111111.11111111
=>
Network:   10.0.0.0/16          00001010.00000000. 00000000.00000000
HostMin:   10.0.0.1             00001010.00000000. 00000000.00000001
HostMax:   10.0.255.254         00001010.00000000. 11111111.11111110
Broadcast: 10.0.255.255         00001010.00000000. 11111111.11111111
Hosts/Net: 65534                 Class A, Private Internet

```

