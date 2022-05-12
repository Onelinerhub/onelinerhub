# Using 2-pass encoding with H.264 codec

```bash
ffmpeg -y -i in.mp4 -c:v libx264 -b:v 2600k -pass 1 -an -f null /dev/null && \
ffmpeg -i in.mp4 -c:v libx264 -b:v 2600k -pass 2 -c:a aac -b:a 128k out.mp4
```

- `ffmpeg` - name of the package to install
- `-i in.mp4` - input video file
- `-c:v libx264` - use H.264 codec
- `-b:v 2600k` - desired bitrate (2.6MBs in our case)
- `-pass 1` - first pass to analyze video
- `-pass 2` - second pass to encode video using collected data
- `-c:a aac` - use [`AAC` codec](/ffmpeg/encode-mp3-to-aac) for audio
- `-b:a 128k` - use 128k bitrate for audio
- `out.mp4` - resulting video file

group: h264

## Example: 
```bash
ffmpeg -hide_banner -f lavfi -i nullsrc -c:v libx264 -preset help -f mp4 - 2>&1 | grep Possible
```
```
[libx264 @ 0x561c3c9d3ec0] Possible presets: ultrafast superfast veryfast faster fast medium slow slower veryslow placebo
[libx264 @ 0x561c3c9d3ec0] Possible tunes: film animation grain stillimage psnr ssim fastdecode zerolatency

```

