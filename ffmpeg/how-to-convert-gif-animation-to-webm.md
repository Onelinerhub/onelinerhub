# How to convert GIF animation to WEBM

```bash
ffmpeg -i in.gif -pix_fmt yuv420p out.webm
```

- `-i in.gif` - input `GIF` animation
- `-pix_fmt yuv420p` - use yuv420p pixel format
- `out.webm` - resulting video file

group: gif


