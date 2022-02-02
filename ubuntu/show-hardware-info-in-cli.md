# Show hardware info in CLI

```bash
apt install inxi
inxi -F
```

- `apt install` - installs specified package on Ubuntu
- `inxi` - powerful system information utility
- `-F` - show full system info

## Example: 
```bash
inxi -F
```
```
System:    Host: ip-172-26-12-191 Kernel: 5.4.0-1018-aws x86_64 bits: 64 Console: tty 0 Distro: Ubuntu 20.04 LTS (Focal Fossa) 
Machine:   Type: Xen System: Xen product: HVM domU v: 4.11.amazon serial: ec26e5af-fa11-3305-5ef9-10f7a7c8d0d7 
           Mobo: N/A model: N/A serial: N/A BIOS: Xen v: 4.11.amazon date: 08/24/2006 
CPU:       Topology: Single Core model: Intel Xeon E5-2686 v4 bits: 64 type: MCP L2 cache: 45.0 MiB 
           Speed: 2300 MHz min/max: N/A Core speed (MHz): 1: 2300 
Graphics:  Device-1: Cirrus Logic GD 5446 driver: N/A 
           Display: server: No display server data found. Headless machine? tty: 140x77 
           Message: Advanced graphics data unavailable in console for root. 
Audio:     Message: No Device data found. 
Network:   Device-1: Intel 82371AB/EB/MB PIIX4 ACPI type: network bridge driver: N/A 
           IF-ID-1: eth0 state: up speed: N/A duplex: N/A mac: 02:ba:70:82:8b:7c 
Drives:    Local Storage: total: 20.00 GiB used: 8.46 GiB (42.3%) 
Partition: ID-1: / size: 19.32 GiB used: 8.46 GiB (43.8%) fs: ext4 dev: /dev/xvda1 
Sensors:   Message: No sensors data was found. Is sensors configured? 
Info:      Processes: 117 Uptime: 295d 21h 05m Memory: 475.4 MiB used: 321.1 MiB (67.5%) Init: systemd runlevel: 5 Shell: bash 
           inxi: 3.0.38 
```

