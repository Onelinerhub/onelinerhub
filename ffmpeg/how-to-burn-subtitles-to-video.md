# How to burn subtitles to video

```bash
ffmpeg -i in.mp4 -vf subtitles=subtitles.srt out.mp4
```

- `-i in.mp4` - input video file
- `-vf` - apply specific video filters
- `subtitles=` - filter allows burning subtitles from specified file
- `subtitles.srt` - path to subtitles file
- `out.mp4` - resulting video file

group: subtitles


