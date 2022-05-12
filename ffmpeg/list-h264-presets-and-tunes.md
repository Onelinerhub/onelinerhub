# How to list H.264 presets and tunes

```bash
ffmpeg -hide_banner -f lavfi -i nullsrc -c:v libx264 -preset help -f mp4 - 2>&1 | grep Possible
```


group: h264

## Example: 
```bash
ffmpeg -hide_banner -f lavfi -i nullsrc -c:v libx264 -preset help -f mp4 - 2>&1 | grep Possible
```
```
[libx264 @ 0x561c3c9d3ec0] Possible presets: ultrafast superfast veryfast faster fast medium slow slower veryslow placebo
[libx264 @ 0x561c3c9d3ec0] Possible tunes: film animation grain stillimage psnr ssim fastdecode zerolatency

```

