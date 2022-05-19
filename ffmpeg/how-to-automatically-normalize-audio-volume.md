# How to automatically normalize audio volume

```bash
ffmpeg-normalize in.mp3 -o out.m4a -c:a aac -b:a 192k
```

- `lib:ffmpeg-normalize` - handly [audio normalization tool](/ffmpeg/how-to-install-ffmpeg-normalize-on-ubuntu-ubuntuversion)
- `in.mp3` - input file to normalize
- `-o out.m4a` - output normalizes audio as `m4a` audio file
- `-c:a aac` - use [`AAC`](/ffmpeg/how-to-set-audio-quality-for-aac) codec for output file
- `-b:a 192k` - use 192k bitrate for output audio

group: ffmpeg-normalize


