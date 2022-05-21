# How to list recording sound devices on PC in Ubuntu

```ffmpeg
arecord -l
```

- `arecord` - ALSA utils tool
- `-l` - will list available sound devices that support recording

group: capture

## Example: 
```ffmpeg
arecord -l
```
```
card 1: Generic [HD-Audio Generic], device 0: ALC887-VD Analog [ALC887-VD Analog]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: Generic [HD-Audio Generic], device 2: ALC887-VD Alt Analog [ALC887-VD Alt Analog]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

link_youtube: https://youtu.be/GG0eGWtLABs
