# Encoding to AV1 codec using average bitrate

```bash
ffmpeg -i in.mp4 -c:v libaom-av1 -b:v 2M out.mkv
```

- `ffmpeg` - name of the package to install
- `-i in.mp4` - input video file
- `-c:v libaom-av1` - use `AV1` video codec
- `-b:v 2M` - target average bitrate is 2Mbit/s
- `out.mkv` - resulting video file

group: av1


