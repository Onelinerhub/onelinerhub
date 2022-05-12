# Using 2-pass encoding for H.265 codec

```bash
ffmpeg -y -i in.mp4 -c:v libx265 -b:v 2600k -x265-params pass=1 -an -f null /dev/null && \
ffmpeg -i in.mp4 -c:v libx265 -b:v 2600k -x265-params pass=2 -c:a aac -b:a 128k out.mp4
```

- `ffmpeg` - name of the package to install
- `-i in.mp4` - input video file
- `-c:v libx265` - use H.265 codec
- `-b:v 2600k` - desired bitrate for video (2.6MBs)
- `x265-params pass=1` - first pass to analyze veideo
- `-x265-params pass=2` - second pass to encode video using computed data
- `-b:a 128k` - use 128k bitrate for audio
- `out.mp4` - resulting video file

group: h265


