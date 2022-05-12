# Convert video to webm using VP9

```bash
ffmpeg -i in.mp4 -c:v libvpx-vp9 -crf 18 -b:v 0 -b:a 128k -c:a libopus out.webm
```

- `ffmpeg` - name of the package to install
- `-i in.mp4` - input video file
- `-c:v libvpx-vp9` - use [VP9](https://en.wikipedia.org/wiki/VP9) Webm codec
- `-crf 18` - preferred quality level (`bitrate`), where `0` is lossless and `51` is worst
- `-b:v 0` - this should be used to set quality with `crf` flag
- `-b:a 128k` - use 128k bitrate for audio
- `-c:a libopus` - use libopus codec for audio
- `out.webm` - resulting video file in WEBM format

group: webm


