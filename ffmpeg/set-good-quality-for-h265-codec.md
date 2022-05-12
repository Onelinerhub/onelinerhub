# Set good quality for H.265 codec

```bash
ffmpeg -i in.mp4 -c:v libx265 -crf 10 -preset slower out.mp4
```

- `ffmpeg` - name of the package to install
- `-i in.mp4` - input video file
- `-crf 10` - set quality level (`bitrate`), where `0` is lossless and `51` is worst
- `-preset slower` - use highly efficient (thus slow) conversion [preset](/ffmpeg/how-to-use-presets) mode
- `out.mp4` - resulting video file

group: h265


