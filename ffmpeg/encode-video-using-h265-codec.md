# Encode video using H.265 codec

```bash
ffmpeg -i in.mp4 -c:v libx265 -crf 26 -preset medium -c:a aac -b:a 128k out.mp4
```

- `ffmpeg` - name of the package to install
- `-i in.mp4` - input video file
- `-c:v libx265` - use H.265 video codec
- `-crf 26` - preferred quality level (`bitrate`), where `0` is lossless and `51` is worst
- `-preset medium` - conversion [preset](/ffmpeg/how-to-use-presets) mode
- `-c:a aac` - use [`AAC`](/ffmpeg/encode-mp3-to-aac) as audio codec
- `-b:a 128k` - use 128k bitrate for audio
- `out.mp4` - resulting video file

group: h265


