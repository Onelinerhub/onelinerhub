# How to list supported pixel formats

```bash
ffmpeg -pix_fmts
```

- `ffmpeg` - basic ffmpeg utility
- `-pix_fmts` - will show supported pixel formats

group: pix_fmt

## Example: 
```bash
ffmpeg -pix_fmts
```
```
Pixel formats:
I.... = Supported Input  format for conversion
.O... = Supported Output format for conversion
..H.. = Hardware accelerated format
...P. = Paletted format
....B = Bitstream format
FLAGS NAME            NB_COMPONENTS BITS_PER_PIXEL
-----
IO... yuv420p                3            12
IO... yuyv422                3            16
IO... rgb24                  3            24
IO... bgr24                  3            24
IO... yuv422p                3            16
IO... yuv444p                3            24
...
```

