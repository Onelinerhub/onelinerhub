# How to convert wav to mp3

```bash
ffmpeg -i in.wav -vn -ar 44100 -b:a 192k out.mp3
```

- `-i in.wav` - input audio file
- `-vn` - skip video (leave only audio)
- `-ar 44100` - set audio sampling to 44k
- `-b:a 192k` - set audio bitrate to 192k
- `out.mp3` - resulting file

group: wav


link_youtube: https://youtu.be/fvoAnxbVKBU
