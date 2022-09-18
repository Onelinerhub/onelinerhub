# How to explain the ip address with netmask.



```bash
ipcalc ip-address/netmask
```

- ipcalc - perform simple manipulation of IP addresses
- ...

## Example

```bash
ipcalc 10.0.0.0/16
```

```bash
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
