# Convert audio file to mp3

```bash
ffmpeg -i in.wav -vn -ar 44100 -ac 2 -ab 192k out.mp3
```

- `-i in.wav` - input audio file
- `-vn` - skip video
- `-ar 44100 -ac 2 -ab 192k` - sets quality of resulting audio, try increasing "ab" and "ar" to get better quality
- `out.mp3` - resulting file

group: convert_audio


link_youtube: https://youtu.be/9pnlIqCljm0
