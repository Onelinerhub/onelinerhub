# Set bitrate for H.265 codec

```bash
ffmpeg -i in.mp4 -c:v libx265 -crf 11 out.mp4
```

- `ffmpeg` - name of the package to install
- `-i in.mp4` - input video file
- `-crf 11` - set bitrate, where `0` is lossless and `51` is worst
- `out.mp4` - resulting video file

group: h265


