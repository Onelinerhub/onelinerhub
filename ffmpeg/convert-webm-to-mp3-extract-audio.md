# Convert Webm to mp3 (extract audio)

```bash
ffmpeg -i in.webm -vn -q:a 0 -map a out.mp3
```

- `ffmpeg` - name of the package to install
- `in.webm` - input video file
- `-vn` - skip video (so extract only audio)
- `-q:a 0` - use best quality for resulting `mp3` file
- `-map a` - extract audio
- `out.mp3` - resulting `mp3` file

group: webm


