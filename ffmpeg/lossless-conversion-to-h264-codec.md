# Lossless conversion using H.264 codec

```bash
ffmpeg -i in.mp4 -c:v libx264 -preset veryslow -qp 0 out.mkv
```

- `ffmpeg` - name of the package to install
- `-i in.mp4` - input video file
- `-c:v libx264` - use H.264 codec
- `-preset` - specify [preset](https://trac.ffmpeg.org/wiki/Encode/H.264#Preset) (mode) to use for conversion, where `ultrafast` is fastest but primitive and `veryslow` is slowest but most efficient
- `-qp 0` - sets quality level to lossless
- `out.mkv` - resulting video file

group: h264

## Example: 
```bash
ffmpeg -hide_banner -f lavfi -i nullsrc -c:v libx264 -preset help -f mp4 - 2>&1 | grep Possible
```
```
[libx264 @ 0x561c3c9d3ec0] Possible presets: ultrafast superfast veryfast faster fast medium slow slower veryslow placebo
[libx264 @ 0x561c3c9d3ec0] Possible tunes: film animation grain stillimage psnr ssim fastdecode zerolatency

```

