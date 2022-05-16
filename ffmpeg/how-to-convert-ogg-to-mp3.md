# How to convert OGG to MP3

```bash
ffmpeg -i in.ogg -vn -ar 44100 -b:a 192k out.mp3
```

- `-i in.ogg` - input audio file to convert
- `-vn` - skip video (leave only audio)
- `-ar 44100` - set audio sampling to 44k
- `-b:a 192k` - set audio bitrate to 192k
- `out.mp3` - resulting audio file

group: ogg


